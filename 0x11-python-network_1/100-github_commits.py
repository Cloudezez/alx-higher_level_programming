#!/usr/bin/python3
import sys
import requests

def fetch_commits(repo_name, owner_name):
    """Fetch and print the 10 most recent commits for a given repository."""
    url = f"https://api.github.com/repos/Cloudezez/alx-higher_level_programming/commits"
    response = requests.get(url)
    
    if response.status_code == 200:
        commits = response.json()
        for commit in commits[:10]:  # Get the most recent 10 commits
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")
    else:
        print("Error: Unable to fetch commits")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./100-github_commits.py alx-higher_level_programming Cloudezez")
    else:
        repo_name = sys.argv[1]
        owner_name = sys.argv[2]
        fetch_commits(repo_name, owner_name)

