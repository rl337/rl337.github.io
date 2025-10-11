#!/usr/bin/env python3
"""
GitHub Repository Analyzer for Jekyll Site
Analyzes public repositories and generates project pages
"""

import os
import json
import requests
import yaml
from datetime import datetime, timedelta
from pathlib import Path
import argparse
import time

class GitHubRepoAnalyzer:
    def __init__(self, username, token=None):
        self.username = username
        self.token = token
        self.session = requests.Session()
        
        if token:
            self.session.headers.update({
                'Authorization': f'token {token}',
                'Accept': 'application/vnd.github.v3+json'
            })
    
    def get_repositories(self):
        """Fetch all public repositories for the user"""
        repos = []
        page = 1
        per_page = 100
        
        while True:
            url = f"https://api.github.com/users/{self.username}/repos"
            params = {
                'type': 'public',
                'sort': 'updated',
                'direction': 'desc',
                'per_page': per_page,
                'page': page
            }
            
            response = self.session.get(url, params=params)
            
            # Handle rate limiting
            if response.status_code == 429:
                print(f"Rate limited. Waiting 60 seconds...")
                time.sleep(60)
                continue
                
            response.raise_for_status()
            
            page_repos = response.json()
            if not page_repos:
                break
                
            repos.extend(page_repos)
            page += 1
            
            # Rate limiting protection - small delay between requests
            time.sleep(0.5)
            
            if len(page_repos) < per_page:
                break
        
        return repos
    
    def analyze_repository(self, repo):
        """Analyze a single repository and extract key information"""
        # Get additional repository details
        repo_details = self.session.get(repo['url']).json()
        
        # Get languages
        languages = self.session.get(repo['languages_url']).json()
        
        # Get recent commits (last 30 days)
        commits_url = f"{repo['url']}/commits"
        commits_response = self.session.get(commits_url, params={
            'since': (datetime.now() - timedelta(days=30)).isoformat(),
            'per_page': 100
        })
        recent_commits = commits_response.json() if commits_response.status_code == 200 else []
        
        # Calculate activity score
        activity_score = self.calculate_activity_score(repo, recent_commits)
        
        # Determine activity level
        activity_level = self.get_activity_level(activity_score, repo)
        
        # Extract key information
        analysis = {
            'name': repo.get('name', 'Unknown'),
            'full_name': repo.get('full_name', 'Unknown'),
            'description': repo.get('description') or 'No description available',
            'url': repo.get('html_url', ''),
            'homepage': repo.get('homepage'),
            'created_at': repo.get('created_at', ''),
            'updated_at': repo.get('updated_at', ''),
            'pushed_at': repo.get('pushed_at', ''),
            'language': repo.get('language'),
            'languages': languages,
            'topics': repo.get('topics', []),
            'stars': repo.get('stargazers_count', 0),
            'forks': repo.get('forks_count', 0),
            'size': repo.get('size', 0),
            'open_issues': repo.get('open_issues_count', 0),
            'license': repo.get('license', {}).get('name') if repo.get('license') else None,
            'archived': repo.get('archived', False),
            'disabled': repo.get('disabled', False),
            'activity_score': activity_score,
            'activity_level': activity_level,
            'recent_commits': len(recent_commits),
            'readme_content': self.get_readme_content(repo),
            'primary_language': max(languages.items(), key=lambda x: x[1])[0] if languages else None,
            'language_percentages': self.calculate_language_percentages(languages)
        }
        
        return analysis
    
    def calculate_activity_score(self, repo, recent_commits):
        """Calculate an activity score based on various factors"""
        score = 0
        
        # Recent commits (last 30 days)
        score += len(recent_commits) * 10
        
        # Recent push (last 7 days = 50 points, last 30 days = 20 points)
        if repo.get('pushed_at'):
            try:
                push_date = datetime.fromisoformat(repo['pushed_at'].replace('Z', '+00:00'))
                days_since_push = (datetime.now(push_date.tzinfo) - push_date).days
                
                if days_since_push <= 7:
                    score += 50
                elif days_since_push <= 30:
                    score += 20
                elif days_since_push <= 90:
                    score += 10
            except (ValueError, TypeError):
                pass  # Skip if date parsing fails
        
        # Stars and forks (community engagement)
        score += (repo.get('stargazers_count') or 0) * 2
        score += (repo.get('forks_count') or 0) * 5
        
        # Open issues (maintenance activity)
        score += (repo.get('open_issues_count') or 0) * 1
        
        # Size (project complexity)
        size = repo.get('size', 0)
        if isinstance(size, (int, float)) and size > 1000:  # Large projects
            score += 5
        
        return score
    
    def get_activity_level(self, score, repo):
        """Determine activity level based on score and other factors"""
        if repo['archived'] or repo['disabled']:
            return 'archived'
        elif score >= 100:
            return 'very_active'
        elif score >= 50:
            return 'active'
        elif score >= 20:
            return 'moderate'
        elif score >= 5:
            return 'low'
        else:
            return 'idle'
    
    def get_readme_content(self, repo):
        """Get README content if available"""
        try:
            readme_url = f"{repo['url']}/readme"
            response = self.session.get(readme_url, headers={'Accept': 'application/vnd.github.v3.html'})
            if response.status_code == 200:
                return response.text[:500] + '...' if len(response.text) > 500 else response.text
        except:
            pass
        return None
    
    def calculate_language_percentages(self, languages):
        """Calculate percentage breakdown of languages"""
        total_bytes = sum(languages.values())
        if total_bytes == 0:
            return {}
        
        return {lang: round((bytes / total_bytes) * 100, 1) 
                for lang, bytes in languages.items()}
    
    def generate_project_frontmatter(self, analysis):
        """Generate Jekyll frontmatter for a project"""
        # Determine if project should be featured (will be overridden by top 5 logic)
        featured = analysis['activity_level'] in ['very_active', 'active'] and analysis['stars'] > 0
        
        # Create technologies list
        technologies = []
        if analysis['primary_language']:
            technologies.append(analysis['primary_language'])
        
        # Add top languages by percentage
        for lang, percentage in sorted(analysis['language_percentages'].items(), 
                                    key=lambda x: x[1], reverse=True)[:3]:
            if lang not in technologies:
                technologies.append(lang)
        
        # Add topics as technologies
        technologies.extend(analysis['topics'][:3])
        
        frontmatter = {
            'title': analysis['name'].replace('-', ' ').replace('_', ' ').title(),
            'description': analysis['description'],
            'technologies': technologies[:5],  # Limit to 5 technologies
            'github': analysis['url'],
            'live_url': analysis['homepage'] if analysis['homepage'] else None,
            'featured': featured,
            'activity_level': analysis['activity_level'],
            'stars': analysis['stars'],
            'forks': analysis['forks'],
            'last_updated': analysis['pushed_at'][:10],  # YYYY-MM-DD format
            'created': analysis['created_at'][:10],
            'language': analysis['primary_language'],
            'license': analysis['license'],
            'archived': analysis['archived']
        }
        
        return frontmatter
    
    def generate_project_content(self, analysis):
        """Generate the main content for a project page"""
        content = f"## {analysis['name'].replace('-', ' ').replace('_', ' ').title()}\n\n"
        content += f"{analysis['description']}\n\n"
        
        # Activity status
        activity_emoji = {
            'very_active': '🔥',
            'active': '⚡',
            'moderate': '📈',
            'low': '📉',
            'idle': '😴',
            'archived': '📦'
        }
        
        content += f"**Status:** {activity_emoji.get(analysis['activity_level'], '❓')} {analysis['activity_level'].replace('_', ' ').title()}\n\n"
        
        # Project stats
        content += "## Project Stats\n\n"
        content += f"- **Stars:** {analysis['stars']}\n"
        content += f"- **Forks:** {analysis['forks']}\n"
        content += f"- **Language:** {analysis['primary_language'] or 'Mixed'}\n"
        if analysis['license']:
            content += f"- **License:** {analysis['license']}\n"
        content += f"- **Created:** {analysis['created_at'][:10]}\n"
        content += f"- **Last Updated:** {analysis['pushed_at'][:10]}\n"
        
        # Language breakdown
        if analysis['language_percentages']:
            content += "\n## Language Breakdown\n\n"
            for lang, percentage in sorted(analysis['language_percentages'].items(), 
                                        key=lambda x: x[1], reverse=True)[:5]:
                content += f"- **{lang}:** {percentage}%\n"
        
        # Topics
        if analysis['topics']:
            content += "\n## Topics\n\n"
            for topic in analysis['topics']:
                content += f"`{topic}` "
            content += "\n"
        
        # Links
        content += "\n## Links\n\n"
        content += f"- [View on GitHub]({analysis['url']})\n"
        if analysis['homepage']:
            content += f"- [Live Demo]({analysis['homepage']})\n"
        
        return content
    
    def save_project_file(self, analysis, output_dir):
        """Save a project analysis as a Jekyll markdown file"""
        frontmatter = self.generate_project_frontmatter(analysis)
        content = self.generate_project_content(analysis)
        
        # Create filename
        filename = f"{analysis['name']}.md"
        filepath = Path(output_dir) / filename
        
        # Write file
        with open(filepath, 'w') as f:
            f.write("---\n")
            f.write(yaml.dump(frontmatter, default_flow_style=False, sort_keys=False))
            f.write("---\n\n")
            f.write(content)
        
        return filepath

def main():
    parser = argparse.ArgumentParser(description='Analyze GitHub repositories and generate Jekyll project pages')
    parser.add_argument('--username', required=True, help='GitHub username')
    parser.add_argument('--token', help='GitHub personal access token (optional, for higher rate limits)')
    parser.add_argument('--output', default='docs/_projects', help='Output directory for project files')
    parser.add_argument('--limit', type=int, help='Limit number of repositories to analyze')
    
    args = parser.parse_args()
    
    # Create output directory
    Path(args.output).mkdir(parents=True, exist_ok=True)
    
    # Initialize analyzer
    analyzer = GitHubRepoAnalyzer(args.username, args.token)
    
    print(f"Fetching repositories for {args.username}...")
    repos = analyzer.get_repositories()
    
    if args.limit:
        repos = repos[:args.limit]
    
    print(f"Analyzing {len(repos)} repositories...")
    
    # Analyze each repository
    analyses = []
    for i, repo in enumerate(repos, 1):
        print(f"Analyzing {i}/{len(repos)}: {repo['name']}")
        try:
            analysis = analyzer.analyze_repository(repo)
            analyses.append(analysis)
        except Exception as e:
            print(f"Error analyzing {repo['name']}: {e}")
            continue
    
    # Sort by activity score (most active first)
    analyses.sort(key=lambda x: x['activity_score'], reverse=True)
    
    # Mark top 5 projects as featured
    for i, analysis in enumerate(analyses[:5]):
        analysis['featured'] = True
    
    # Save project files
    print(f"Saving {len(analyses)} project files...")
    for analysis in analyses:
        try:
            filepath = analyzer.save_project_file(analysis, args.output)
            print(f"Saved: {filepath}")
        except Exception as e:
            print(f"Error saving {analysis['name']}: {e}")
    
    # Generate summary
    print("\n" + "="*50)
    print("ANALYSIS SUMMARY")
    print("="*50)
    
    activity_counts = {}
    for analysis in analyses:
        level = analysis['activity_level']
        activity_counts[level] = activity_counts.get(level, 0) + 1
    
    for level, count in sorted(activity_counts.items(), 
                             key=lambda x: ['very_active', 'active', 'moderate', 'low', 'idle', 'archived'].index(x[0])):
        print(f"{level.replace('_', ' ').title()}: {count}")
    
    print(f"\nTotal repositories analyzed: {len(analyses)}")
    print(f"Project files saved to: {args.output}")

if __name__ == '__main__':
    main()
