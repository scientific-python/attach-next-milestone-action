import requests
import argparse
from packaging.version import Version, InvalidVersion

parser = argparse.ArgumentParser()
parser.add_argument('owner_repo')
args = parser.parse_args()

owner, repo = args.owner_repo.split('/')


def is_version(v):
    try:
        Version(v)
        return True
    except InvalidVersion:
        return False


# Get the list of milestones for the repository
milestones_url = f'https://api.github.com/repos/{owner}/{repo}/milestones'
response = requests.get(milestones_url)
milestones = response.json()
milestones = [m for m in milestones if is_version(m['title'])]
milestones = sorted(milestones, key=lambda x: Version(x['title']))

print(milestones[0]['number'])
