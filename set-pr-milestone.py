import os
import requests
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('owner_repo')
parser.add_argument('pr')
parser.add_argument('milestone_nr')
parser.add_argument('--force', action='store_true')
args = parser.parse_args()

owner, repo = args.owner_repo.split('/')

query_url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{args.pr}"
patch_url = f"https://api.github.com/repos/{owner}/{repo}/issues/{args.pr}"

headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"Bearer {os.environ['GH_TOKEN']}",
    "X-GitHub-Api-Version": "2022-11-28"
}

response = requests.get(query_url).json()

if response.get("message") == "Not Found":
    print(f"Error: PR {args.pr} not found on {args.owner_repo}")
    sys.exit(1)

if response["milestone"] and not args.force:
    print("PR already has a milestone; exiting")
    sys.exit(0)

if not response["merged"]:
    print("PR hasn't been merged; not attaching milestone")
    sys.exit(0)

response = requests.patch(
    patch_url,
    json={"milestone": int(args.milestone_nr)},
    headers=headers
)

# Check for errors
response.raise_for_status()

if response.json()['milestone'] is None:
    print("ERROR: could not set milestone")
    sys.exit(1)

print(f"Milestone set on {args.owner_repo} #{args.pr}")
