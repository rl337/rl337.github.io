# GitHub Repository Analysis Scripts

This directory contains scripts to automatically analyze your GitHub repositories and generate project pages for your Jekyll site.

## Quick Start

### Manual Update

Run the update script to analyze your repositories and generate project pages:

```bash
# From the repository root
./scripts/update_projects.sh
```

### With GitHub Token (Recommended)

For higher rate limits and better analysis, set your GitHub token:

```bash
export GITHUB_TOKEN=your_github_token_here
./scripts/update_projects.sh
```

## How It Works

### Repository Analysis

The `analyze_repos.py` script:

1. **Fetches** all your public GitHub repositories
2. **Analyzes** each repository for:
   - Activity level (commits, pushes, stars, forks)
   - Primary programming languages
   - Project metadata (description, topics, license)
   - Recent activity (last 30 days)
3. **Ranks** repositories by activity score
4. **Generates** Jekyll project pages with frontmatter

### Activity Levels

Repositories are categorized by activity level:

- 🔥 **Very Active**: High recent activity, many stars/forks
- ⚡ **Active**: Regular updates and community engagement
- 📈 **Moderate**: Some recent activity
- 📉 **Low**: Minimal recent activity
- 😴 **Idle**: No recent activity
- 📦 **Archived**: Repository is archived

### Generated Files

Each repository becomes a markdown file in `docs/_projects/` with:

- **Frontmatter**: Jekyll metadata (title, description, technologies, etc.)
- **Content**: Project description, stats, language breakdown, links
- **Activity indicators**: Visual status and activity level

## Automation

### GitHub Actions

The repository includes a GitHub Actions workflow (`.github/workflows/update-projects.yml`) that:

- **Runs weekly** (Sundays at 2 AM UTC)
- **Can be triggered manually** via GitHub Actions tab
- **Automatically commits** updated project files
- **Uses your GitHub token** for higher rate limits

### Manual Trigger

To manually trigger the workflow:

1. Go to the **Actions** tab in your GitHub repository
2. Select **Update GitHub Projects** workflow
3. Click **Run workflow**

## Configuration

### Environment Variables

- `GITHUB_TOKEN`: Your GitHub personal access token (optional but recommended)

### Script Options

```bash
python analyze_repos.py --help
```

Options:
- `--username`: GitHub username (required)
- `--token`: GitHub personal access token
- `--output`: Output directory for project files
- `--limit`: Limit number of repositories to analyze

### Customization

You can customize the analysis by modifying:

- **Activity scoring** in `calculate_activity_score()`
- **Activity levels** in `get_activity_level()`
- **Project frontmatter** in `generate_project_frontmatter()`
- **Content generation** in `generate_project_content()`

## Requirements

- Python 3.7+
- `requests` library
- `PyYAML` library

Install with:
```bash
pip install -r requirements.txt
```

## GitHub Token Setup

To get a GitHub personal access token:

1. Go to GitHub Settings → Developer settings → Personal access tokens
2. Generate a new token with `public_repo` scope
3. Add it as a repository secret named `GITHUB_TOKEN`
4. Or set it as an environment variable when running locally

## Troubleshooting

### Rate Limiting

Without a GitHub token, you're limited to 60 requests per hour. With a token, you get 5,000 requests per hour.

### Large Repository Count

If you have many repositories, consider using the `--limit` option to analyze only the most recent ones.

### Missing Dependencies

Make sure to install the required Python packages:
```bash
cd scripts
pip install -r requirements.txt
```

## Output Example

The script generates files like:

```markdown
---
title: "My Awesome Project"
description: "A cool project I built"
technologies: [Python, JavaScript, React]
github: https://github.com/username/project
featured: true
activity_level: very_active
stars: 42
forks: 8
last_updated: 2024-01-15
---

## My Awesome Project

A cool project I built

**Status:** 🔥 Very Active
**Stars:** 42 | **Forks:** 8
**Language:** Python
...
```

This creates a comprehensive, automatically-updated showcase of your GitHub activity!
