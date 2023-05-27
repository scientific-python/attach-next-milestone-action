import os
import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('owner_repo')
args = parser.parse_args()

owner, repo = args.owner_repo.split('/')

# Get the list of milestones for the repository
milestones_url = f'https://api.github.com/repos/{owner}/{repo}/milestones'
response = requests.get(milestones_url)
milestones = response.json()
milestones = sorted(milestones, key=lambda x: x['title'])

print(milestones[0]['number'])
