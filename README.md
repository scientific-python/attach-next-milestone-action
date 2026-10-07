# Attach Next Milestone Action

This action attaches the next open milestone to merged PRs.

Currently, this action only looks at milestones that can be parsed as
version numbers.

A typical job would look like this:

```yaml
# .github/workflows/milestone-merged-prs.yaml

name: Milestone

# Required to update merged PRs originating from forks.
# This workflow must never check out or execute PR-controlled code.
on: # zizmor: ignore[dangerous-triggers]
  pull_request_target:
    types:
      - closed
    branches:
      - 'main'

permissions: {}

jobs:
  milestone_pr:
    name: attach to PR
    if: >-
      github.repository == 'OWNER/REPOSITORY' &&
      github.event.pull_request.merged == true
    runs-on: ubuntu-latest

    permissions:
      issues: write
      pull-requests: read

    steps:
      - uses: scientific-python/attach-next-milestone-action@a4889cfde7d2578c1bc7400480d93910d2dd34f6
        with:
          token: ${{ github.token }}
```

## Options

In the `with` clause, the following options are available:

- `force: true` : Overwrite existing milestones.

## Security

This workflow uses `pull_request_target` to update merged pull requests from forks.
It runs in the base repository's context, where it can receive a write-capable `GITHUB_TOKEN` and access explicitly referenced repository or organization secrets.

The example grants `GITHUB_TOKEN` only the permissions needed to read pull requests and update milestones.
No manually created token or repository secret is required.

Do not check out, build, test, import, or otherwise execute code from the pull request.
Doing so could give the pull request author access to the workflow's token or referenced secrets.
Use only trusted actions that operate on pull request metadata.
