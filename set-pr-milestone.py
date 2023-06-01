import os
import requests
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('owner_repo')
parser.add_argument('pr')
parser.add_argument('milestone_nr')
args = parser.parse_args()

owner, repo = args.owner_repo.split('/')

query_url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{args.pr}"
patch_url = f"https://api.github.com/repos/{owner}/{repo}/issues/{args.pr}"

headers = {
    "Accept": "application/vnd.github.v3+json",
    "Authorization": f"token {os.environ['GH_TOKEN']}",
}

response = requests.get(query_url)

if not response.json()["merged"]:
    print("\nPR was closed without being merged; not attaching milestone\n")
    sys.exit(0)

response = requests.patch(
    patch_url,
    json={"milestone": int(args.milestone_nr)},
    headers=headers
)

# Check for errors
response.raise_for_status()
