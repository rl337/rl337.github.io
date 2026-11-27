#!/bin/bash
# The same required checks run locally in Docker, on PRs, and before deployment.
set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")"
if [ ! -f /.dockerenv ] && [ -z "${DOCKER_CONTAINER:-}" ]; then
    echo "Run ./docker-run.sh ./run_checks.sh to use the project environment."
    exit 1
fi
python3 -m pip install -r scripts/requirements.txt
(cd docs; if ! bundle check; then bundle install; fi)
python3 -m compileall -q scripts
flake8 scripts/analyze_repos.py scripts/tests --max-line-length=100 --ignore=E501,W503
black --check scripts/analyze_repos.py scripts/tests
isort --check-only scripts/analyze_repos.py scripts/tests
mypy scripts/analyze_repos.py --ignore-missing-imports
find . -name '*.sh' -not -path './docs/vendor/*' -not -path './scripts/venv/*' \
    -not -path './docs/_site/*' -exec shellcheck --exclude=SC1091 {} +
find . -name '*.sh' -not -path './docs/vendor/*' -not -path './scripts/venv/*' \
    -not -path './docs/_site/*' -exec bash -n {} +
find docs -type f \( -name '*.md' -o -name '*.markdown' \) \
    -not -path '*/_site/*' -not -path '*/vendor/*' \
    -exec markdownlint --config .markdownlint.json {} +
python3 -c 'import yaml; from pathlib import Path; [yaml.safe_load(p.read_text()) for p in [Path("docs/_config.yml"), *Path("docs/_data").glob("*.yml"), *Path(".github/workflows").glob("*.yml")]]'
# Remove stale output, then build with the same plugins and environment as production.
(cd docs && bundle exec jekyll clean && JEKYLL_ENV=production bundle exec jekyll doctor && JEKYLL_ENV=production bundle exec jekyll build --strict_front_matter --trace)
CHECK_BUILT_SITE=1 python3 -m pytest scripts/tests -v \
    --cov=analyze_repos --cov-report=term-missing --cov-report=xml:scripts/coverage.xml
test -f AGENTS.md && test -f README.md && test -f docs/_config.yml
test -x run_checks.sh && test -x scripts/update_projects.sh
# Preserve the source-secret check; report paths rather than matching values.
python3 - <<'CHECK'
import re
from pathlib import Path
excluded = {'.git', '.env', 'venv', 'vendor', '_site', '__pycache__', '.mypy_cache', '.pytest_cache'}
pattern = re.compile(r'(?:password|secret|api_key|private_key|access_token)\s*=')
failures = []
for path in Path('.').rglob('*'):
    if not path.is_file() or excluded.intersection(path.parts):
        continue
    try:
        lines = path.read_text().splitlines()
    except (UnicodeError, OSError):
        continue
    if any(pattern.search(line) and not any(s in line for s in ['GITHUB_TOKEN', 'fake_', 'test_', 'example_']) for line in lines):
        failures.append(str(path))
if failures:
    raise SystemExit('Potential sensitive assignments in: ' + ', '.join(failures))
CHECK
echo "All required checks passed."
