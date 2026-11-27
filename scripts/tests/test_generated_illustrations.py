"""Validate the revised project notes, retained URLs, and generated artwork."""

import ast
import hashlib
import json
import os
import re
from html.parser import HTMLParser
from pathlib import Path
from xml.etree import ElementTree

import pytest
import yaml
from PIL import Image

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "docs"
SITE = DOCS / "_site"
MANIFEST = ROOT / "scripts/imagegen/crow-illustrations.json"


def recipe():
    return json.loads(MANIFEST.read_text())


def test_generated_assets_match_their_recipes():
    manifest = recipe()
    assert manifest["model"] == "Qwen-Image 2.1"
    images = manifest["images"]
    assert len(images) == len(manifest["posts"])
    assert len({entry["filename"] for entry in images}) == len(images)
    assert len({entry["seed"] for entry in images}) == len(images)
    for entry in images:
        path = DOCS / "assets/images/blog" / entry["filename"]
        with Image.open(path) as image:
            assert image.format == "WEBP"
            assert image.size == (manifest["width"], manifest["height"])
            image.verify()
        assert hashlib.sha256(path.read_bytes()).hexdigest() == entry["sha256"]
        assert len(entry["alt"]) > 20
        assert "crow" in entry["prompt"].lower()
        assert not (path.parent / entry["source_filename"]).exists()


def test_retained_notes_preserve_metadata_and_remove_checklist_status_copy():
    manifest = recipe()
    for name, entry in manifest["posts"].items():
        text = (DOCS / "_posts" / name).read_text()
        _, raw, body = text.split("---", 2)
        metadata = yaml.safe_load(raw)
        for key, expected in entry["preserved_metadata"].items():
            actual = str(metadata[key]) if key == "date" else metadata[key]
            assert actual == expected, (name, key)
        assert metadata["permalink"] == entry["permalink"]
        assert metadata["tags"] == entry["tags"]
        assert str(metadata["last_modified_at"]) == "2026-11-27"
        assert not re.search(r"(?m)^\s*[-*+]\s+\[[ xX]\]", body)
        assert not re.search(
            r"(?im)^#{1,6}\s+.*(?:project status|current features|planned features|key features|roadmap)",
            body,
        )
        assert "https://github.com/rl337/the-dark-closet" not in body
        assert "https://github.com/rl337/trouble" not in body
        assert body.count('<figure class="post-illustration">') == 1


class ImageElements(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.images = {}
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        if tag == "img":
            attrs = dict(attrs)
            self.images[attrs.get("src")] = attrs


@pytest.mark.skipif(
    os.environ.get("CHECK_BUILT_SITE") != "1",
    reason="Requires the production build from run_checks.sh",
)
def test_every_retained_illustration_renders_at_the_original_article_url():
    manifest = recipe()
    expected = {
        "/assets/images/blog/" + entry["filename"]: entry["alt"]
        for entry in manifest["images"]
    }
    found = {}
    for post in manifest["posts"].values():
        page = SITE / post["permalink"].lstrip("/")
        assert page.is_file(), page
        text = page.read_text()
        assert "Revised November 27, 2026." in text
        for url, attrs in ImageElements(text).images.items():
            if url in expected:
                assert url not in found
                assert attrs.get("alt") == expected[url]
                assert attrs.get("width") == "1280"
                assert attrs.get("height") == "720"
                assert attrs.get("loading") == "eager"
                assert attrs.get("decoding") == "async"
                assert (SITE / url.lstrip("/")).is_file()
                found[url] = page
    assert found.keys() == expected.keys()


@pytest.mark.skipif(
    os.environ.get("CHECK_BUILT_SITE") != "1",
    reason="Requires the production build from run_checks.sh",
)
def test_retired_post_redirects_and_obsolete_directory_references_are_removed():
    manifest = recipe()
    for url in manifest["retired_urls"]:
        page = SITE / url.lstrip("/")
        text = page.read_text()
        assert 'http-equiv="refresh" content="0;url=/writing/"' in text
        assert '<meta name="robots" content="noindex">' in text
        for index in [
            "writing/index.html",
            "archives/index.html",
            "sitemap.xml",
            "feed.xml",
        ]:
            assert url not in (SITE / index).read_text()
    projects = (SITE / "projects/index.html").read_text()
    assert "https://rl337.org/trouble/" not in projects
    assert "https://github.com/rl337/trouble" not in projects
    assert "https://rl337.org/pale-blue-dot/" not in projects


def test_examples_are_valid_python_and_architecture_is_static_svg():
    for name in recipe()["posts"]:
        text = (DOCS / "_posts" / name).read_text()
        examples = re.findall(r"```python\n(.*?)```", text, re.DOTALL)
        assert len(examples) == 1
        ast.parse(examples[0])
    path = DOCS / "assets/images/blog/june-architecture.svg"
    diagram = ElementTree.fromstring(path.read_text())
    assert diagram.attrib["width"] == "1600"
    assert diagram.attrib["height"] == "533"
    labels = " ".join(diagram.itertext())
    assert "MechaHarness" in labels
    assert "TaskRunner + client" in labels
    assert "Goals + work records" in labels
    for element in diagram.iter():
        assert element.tag.split("}")[-1] not in {"script", "foreignObject", "image"}
        assert not any(key.lower().startswith("on") for key in element.attrib)
