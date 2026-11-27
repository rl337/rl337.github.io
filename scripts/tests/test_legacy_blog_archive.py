"""Content checks for the restored WordPress posts."""

import re
from pathlib import Path
from urllib.parse import unquote

import yaml

DOCS = Path(__file__).resolve().parents[2] / "docs"


def test_restored_posts_keep_original_urls_and_local_media():
    paths = set()
    for post in (DOCS / "_posts").glob("*.md"):
        _, raw_front_matter, body = post.read_text(encoding="utf-8").split("---", 2)
        metadata = yaml.safe_load(raw_front_matter)
        if not metadata.get("legacy_archive"):
            continue
        permalink = metadata["permalink"]
        # WordPress's date-based permalink must still resolve after the migration.
        assert permalink.startswith(f"/{str(metadata['date']).replace('-', '/')}/")
        assert permalink.endswith("/")
        assert permalink not in paths
        paths.add(permalink)
        assert metadata["archive_source"].startswith("https://web.archive.org/web/")
        assert metadata["archive_source"] in body
        for location in re.findall(r"(/assets/(?:images|audio)/legacy-blog/[^)\s]+)", body):
            assert (DOCS / unquote(location.lstrip("/"))).is_file(), (post, location)
    assert {
        "/2011/09/13/submediant-the-voice-of-robots/",
        "/2011/11/03/hello-sena-the-script/",
        "/2014/02/23/building-infrastructure-in-chuck/",
    } <= paths
