"""Preserve the original articles while rendering recovery context separately."""

import hashlib
import json
import re
from pathlib import Path
from urllib.parse import unquote

import yaml

DOCS = Path(__file__).resolve().parents[2] / "docs"
FIXTURE = Path(__file__).parent / "fixtures" / "legacy_manifest.json"


def read_post(path):
    _, raw, body = path.read_text(encoding="utf-8").split("---", 2)
    return yaml.safe_load(raw), body


def test_restored_posts_preserve_metadata_prose_and_recovery_notes():
    manifest = json.loads(FIXTURE.read_text())
    restored = {}
    for post in (DOCS / "_posts").glob("*"):
        metadata, body = read_post(post)
        if metadata.get("legacy_archive"):
            restored[post.name] = (metadata, body)
    assert len(restored) == 85
    assert restored.keys() == manifest.keys()
    for name, (metadata, body) in restored.items():
        expected = manifest[name]
        original_metadata = dict(metadata)
        notes = original_metadata.pop("recovery_notes", "")
        assert original_metadata == expected["metadata"], name
        assert (
            hashlib.sha256(body.strip().encode()).hexdigest()
            == expected["article_sha256"]
        ), name
        assert (
            hashlib.sha256(notes.strip().encode()).hexdigest()
            == expected["recovery_sha256"]
        ), name
        assert "Originally published on " not in body
        assert "[legacy-source]:" not in body


def test_restored_posts_keep_original_urls_and_local_media():
    paths = set()
    for post in (DOCS / "_posts").glob("*"):
        metadata, body = read_post(post)
        if not metadata.get("legacy_archive"):
            continue
        permalink = metadata["permalink"]
        assert permalink.startswith(f"/{str(metadata['date']).replace('-', '/')}/")
        assert permalink.endswith("/")
        assert permalink not in paths
        paths.add(permalink)
        assert metadata["archive_source"].startswith("https://web.archive.org/web/")
        text = body + metadata.get("recovery_notes", "")
        for location in re.findall(
            r"(/assets/(?:images|audio)/legacy-blog/[^)\s]+)", text
        ):
            assert (DOCS / unquote(location.lstrip("/"))).is_file(), (post, location)
    assert {
        "/2011/09/13/submediant-the-voice-of-robots/",
        "/2011/11/03/hello-sena-the-script/",
        "/2014/02/23/building-infrastructure-in-chuck/",
    } <= paths


def test_present_day_notes_require_their_own_dates():
    for post in (DOCS / "_posts").glob("*"):
        metadata, _ = read_post(post)
        if metadata.get("present_day_note"):
            assert metadata.get("present_day_note_date"), post
