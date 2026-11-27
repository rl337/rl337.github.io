# rl337.org

Richard Lee's personal blog, built with Jekyll and hosted on GitHub Pages.
Substack is the separate home for semi-professional writing.

## Develop and validate

Use Docker for project commands:

```bash
docker build -t rl337-dev .
./docker-run.sh ./run_checks.sh
./docker-run.sh bash -c 'cd docs && bundle exec jekyll serve --host 0.0.0.0'
```

For a browser preview, publish container port 4000, for example:

```bash
docker run --rm -p 127.0.0.1:4000:4000 -v "$PWD":/workspace -w /workspace rl337-dev \
  bash -c 'cd docs && bundle install && bundle exec jekyll serve --host 0.0.0.0'
```

Open http://127.0.0.1:4000. The required checks build a fresh production site,
test the generated pages and archive routes, check restored content preservation,
and run Python, shell, Markdown, and YAML checks. PRs run the same script.
Deployment publishes that validated output after a merge to main.

## Personal writing

Add a Markdown file in `docs/_posts/` named `YYYY-MM-DD-title.md`:

```yaml
---
layout: post
title: A specific title
date: 2026-11-27
---
```

Use the editorial guides in the sibling `socials` project for Richard's voice.
Do not invent personal experiences or turn project documentation into personal claims.
The homepage introduces the blog; `/writing/` lists newer posts, and `/archives/`
includes every post.

## Restored articles

The 85 recovered articles retain their original dates, permalinks, attribution,
prose, and media references. Their common presentation lives in
`docs/_layouts/post.html`, activated by `legacy_archive: true`.

Required metadata: `title`, `date`, `author`, `permalink`, `legacy_archive`,
`archive_source`, and `archive_original_timestamp`. Keep the original timestamp
as provenance; the article's visible publication date comes from `date`.

Recovery boilerplate belongs in the template, not the article body.
Use optional Markdown `recovery_notes` for missing media or recovery limitations.
An optional `present_day_note` requires `present_day_note_date`; both render
separately from the historical article. These fields must contain actual supplied
commentary, never a generated retrospective attributed to Richard.

Preservation fingerprints in `scripts/tests/fixtures/legacy_manifest.json`
capture the original metadata, article text, and recovered notes at migration.
Investigate failures rather than regenerating the fixture to accept accidental edits.
Any intentional historical correction requires review and a matching fixture update.

## Curated projects

Edit `docs/_data/projects.yml`. This catalog is the only source for current
project listings. The old repository analyzer remains an optional discovery tool;
its generated `_projects` collection is excluded from the site and cannot replace
the curated selection.

Each entry has `featured` (true for highlights), `title`, `kind`, `summary`, `description`, `site_url`, and
`site_label`. Optional `repository` links source code. `substack_tags` is an
array of `{title, url}` entries using verified public tag URLs.
Optional `substack_posts` uses the same shape for verified individual articles.
Leave unknown or nonexistent tags empty; never manufacture tag pages.

The public-repository audit on 2026-11-27 found Pages sites for Mechaharness,
Metro, pyiv, c10y, and this website. Richard explicitly excluded c10y and requested
Submediant, which links to its restored archive until a current public site exists.
A subsequent authenticated audit also found reachable public sites for Confidence
and CorbyCarby. These appear in the secondary published-site list without links to private
source repositories. References to the two retired project sites were removed. Submediant has Pages configured, but its
expected public URL returned 404 during verification.
This is a manually maintained selection, not a claim of perpetual completeness.
Recheck public repositories and final site URLs when updating the catalog.

The public Substack feed currently exposes one article about pyiv. Its public
metadata has an empty `postTags` array, so the catalog links that article directly.
Tag mappings can be added as Richard establishes them.

## Visual style

`docs/assets/main.scss` owns the shared Watercolor CSS, based on
`socials/tools/studio/assets/skins.css`. Keep dark, readable text and visible
keyboard focus against the soft background and pastel surfaces. Shared layouts
cover personal pages, current posts, restored articles, and taxonomy archives.

## Project notes and crow illustrations

The three retained January 2025 project posts (Curioshelf, June, and Metro) were rewritten
using the Richard Lee editorial guides in the sibling `socials` project. Facts were checked
against the repositories' current contents. The two obsolete writeups and their project-directory
links were removed; both old article URLs redirect to the writing index.

The revised posts keep their original dates and have explicit permalinks matching their existing
addresses. A visible revision date distinguishes the rewrite from the original publication.
Keep invented experiences, feature inventories, random checklists, and project-status reports out
of these posts. Use verified details and supplied personal observations instead.

Each retained note uses one conceptual crow illustration generated with Qwen-Image 2.1.
The public prompt, seed, model, output hash, and encoding manifest lives in
`scripts/imagegen/crow-illustrations.json`. Original PNG generations, unused variations,
and service job state are local-only under `.env/crow-imagegen/`; the website serves
optimized WebP copies. The Metro note also uses its explicitly identified 2011 settlement sketch.

Generation used the existing Qwen-Image 2.1 ComfyUI workflow. Configure its endpoint locally;
do not put private service addresses or credentials in the public manifest. The old
Midjourney/placeholder scripts are legacy utilities and should not replace the new illustrations.
Tests validate retained metadata and URLs, generated image references, removal of the obsolete
project links and status/checklist sections, and preservation of the 85 original archive posts.

The three revised project notes include small Python examples checked against their
current source. June also includes a conceptual architecture SVG exported from
the shared socials visualization studio with the Watercolor skin. Its editable
composition is kept locally under socials/.env/diagrams/.
