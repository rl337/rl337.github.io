"""Check the production artifact, including routes the safe build omits."""

import os
import shutil
import subprocess
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "docs"
SITE = DOCS / "_site"
pytestmark = pytest.mark.skipif(
    os.environ.get("CHECK_BUILT_SITE") != "1",
    reason="Run run_checks.sh to build fresh production output first",
)


class Elements(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.links = []
        self.resources = []
        self.ids = set()
        self.headings = []
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.add(attrs["id"])
        if tag == "a":
            self.links.append(attrs.get("href", ""))
        if tag in {"img", "audio", "source", "link"}:
            self.resources.append(attrs.get("src", attrs.get("href", "")))


def output(path, destination=SITE):
    target = destination / unquote(path.lstrip("/"))
    return target / "index.html" if target.is_dir() else target


def assert_local_links_resolve(text, current, destination=SITE):
    parsed = Elements(text)
    for href in parsed.links:
        parts = urlsplit(href)
        if parts.scheme or parts.netloc:
            continue
        if parts.path:
            target = (
                output(parts.path, destination)
                if parts.path.startswith("/")
                else current.parent / parts.path
            )
            if target.is_dir():
                target /= "index.html"
        else:
            target = current
        assert target.is_file(), (current, href)
        if parts.fragment and target.suffix == ".html":
            assert unquote(parts.fragment) in Elements(target.read_text()).ids, (
                current,
                href,
            )


def test_navigation_archive_and_taxonomy_routes():
    routes = ["/", "/about/", "/projects/", "/archives/", "/writing/", "/404.html"]
    routes.extend(
        "/" + str(p.relative_to(SITE))
        for folder in ["categories", "tags"]
        for p in (SITE / folder).rglob("index.html")
    )
    assert (SITE / "categories/submediant/index.html").is_file()
    assert (SITE / "tags/blender/index.html").is_file()
    for route in routes:
        page = output(route)
        text = page.read_text()
        assert 'href="/assets/main.css"' in text
        assert 'href="#main"' in text
        assert 'aria-label="Main navigation"' in text
        assert_local_links_resolve(text, page)
    home = output("/").read_text()
    assert "Life, projects, and" in home
    assert "sugar-glider" not in home
    assert "View all projects →" not in home
    assert "aria-current=" in output("/about/").read_text()
    assert (SITE / "feed.xml").is_file()
    assert (SITE / "sitemap.xml").is_file()


def test_every_restored_article_is_rendered_and_listed():
    archive = output("/archives/").read_text()
    for post in (DOCS / "_posts").glob("*"):
        _, raw, _ = post.read_text().split("---", 2)
        metadata = yaml.safe_load(raw)
        if not metadata.get("legacy_archive"):
            continue
        address = metadata["permalink"]
        assert address in archive, post
        rendered = output(address).read_text()
        assert "From the original blog" in rendered
        assert metadata["archive_source"] in Elements(rendered).links
        assert "Originally published " in rendered
        assert "[legacy-source]" not in rendered
        if metadata.get("recovery_notes"):
            assert '<h2 id="recovery-heading">Recovery notes</h2>' in rendered
            article = rendered.split('<div class="post-content prose">', 1)[1].split(
                "</div>", 1
            )[0]
            assert "The original Flash audio was not recovered." not in article
        else:
            assert 'id="recovery-heading"' not in rendered
        assert 'id="note-heading"' not in rendered
        # Footers are template-owned; original article links may be historical.
        footer = rendered.split('<footer class="post-footer">', 1)[1].split(
            "</footer>", 1
        )[0]
        assert_local_links_resolve(footer, output(address))
        for resource in Elements(rendered).resources:
            path = urlsplit(resource).path
            if path.startswith("/assets/"):
                assert output(path).is_file(), (post, resource)
    assert (SITE / "assets/audio/legacy-blog/echoes-of-sputnik-re-render.mp3").is_file()


def test_curated_project_links_and_watercolor_styles():
    projects = yaml.safe_load((DOCS / "_data/projects.yml").read_text())
    names = {p["title"] for p in projects if p["featured"]}
    assert names == {"Mechaharness", "pyiv", "Metro", "Submediant"}
    links = Elements(output("/projects/").read_text()).links
    for project in projects:
        assert project["site_url"] in links
        if project.get("repository"):
            assert project["repository"] in links
        for tag in project.get("substack_tags", []) + project.get("substack_posts", []):
            assert tag["url"] in links
    css = (SITE / "assets/main.css").read_text()
    assert "#fcfbf8" in css
    assert "#46525a" in css
    assert "focus-visible" in css
    assert "overflow: auto" in css or "overflow:auto" in css
    assert not (SITE / "_projects").exists()
    assert not list(SITE.rglob(".env"))
    assert "connect.sid" not in output("/projects/").read_text()


def test_optional_notes_and_tag_links_render_separately(tmp_path):
    # A temporary source exercises optional fields without publishing fake commentary.
    source = tmp_path / "source"
    destination = tmp_path / "built"
    shutil.copytree(
        DOCS,
        source,
        ignore=shutil.ignore_patterns("vendor", "_site", ".jekyll-cache", ".bundle"),
    )
    fixture = source / "_posts/2010-01-01-template-fixture.md"
    fixture.write_text(
        "---\nlayout: post\ntitle: Template fixture\ndate: 2010-01-01\n"
        "permalink: /template-fixture/\nlegacy_archive: true\n"
        "archive_source: https://web.archive.org/web/20100101/http://example.org/\n"
        "recovery_notes: 'A **missing** download.'\n"
        "present_day_note: 'A **separate** retrospective.'\n"
        "present_day_note_date: 2026-11-27\n---\n\nOriginal article body.\n"
    )
    projects_path = source / "_data/projects.yml"
    projects = yaml.safe_load(projects_path.read_text())
    projects[0]["substack_tags"] = [
        {"title": "A & B", "url": "https://example.org/t/fixture"}
    ]
    projects_path.write_text(yaml.safe_dump(projects))
    subprocess.run(
        [
            "bundle",
            "exec",
            "jekyll",
            "build",
            "--source",
            str(source),
            "--destination",
            str(destination),
        ],
        cwd=DOCS,
        check=True,
        capture_output=True,
        text=True,
    )
    text = output("/template-fixture/", destination).read_text()
    assert "Original article body." in text
    assert "A <strong>missing</strong> download." in text
    assert "A <strong>separate</strong> retrospective." in text
    assert (
        text.index("Original article body.")
        < text.index('id="recovery-heading"')
        < text.index('id="note-heading"')
    )
    assert "January 1, 2010" in text
    assert "November 27, 2026" in text
    assert 'datetime="2026-11-27"' in text
    project_text = output("/projects/", destination).read_text()
    assert "https://example.org/t/fixture" in Elements(project_text).links
    assert "Substack: A &amp; B" in project_text
