import os
import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('owner_repo')
parser.add_argument('pr')
parser.add_argument('milestone_nr')
args = parser.parse_args()

owner, repo = args.owner_repo.split('/')

url = f"https://api.github.com/repos/{owner}/{repo}/issues/{args.pr}"
headers = {
    "Accept": "application/vnd.github.v3+json",
    "Authorization": f"token {os.environ['GH_TOKEN']}",
}

response = requests.patch(
    url,
    json={"milestone": int(args.milestone_nr)},
    headers=headers
)

# Check for errors
response.raise_for_status()
