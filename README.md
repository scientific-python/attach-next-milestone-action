# Attach Next Milestone Action

This action attaches the next open milestone to merged PRs.

Currently, this action only looks at milestones that can be parsed as
version numbers.

A typical job would look like this:

```yaml
# .github/workflows/milestone-merged-prs.yaml

name: Milestone

on:
  push:
    branches:
      - 'main'

permissions: {}

jobs:
  milestone_pr:
    name: attach to PR
    if: github.repository == 'OWNER/REPOSITORY'
    runs-on: ubuntu-latest

    permissions:
      issues: write
      pull-requests: read

    steps:
      - uses: scientific-python/attach-next-milestone-action@a4889cfde7d2578c1bc7400480d93910d2dd34f6
        with:
          token: ${{ github.token }}
```

The action finds the merged PR that belongs to the pushed commit.
Pushes without a merged PR, such as direct commits to `main`, are skipped.

## Options

In the `with` clause, the following options are available:

- `force: true` : Overwrite existing milestones.

## Security

The workflow runs on `push`, so it executes only code that is already on your main branch.
It does not need `pull_request_target`, and it does not run code from pull requests.

The example grants `GITHUB_TOKEN` only the permissions needed to read pull requests and update milestones.
No manually created token or repository secret is required.

## Migrating from `pull_request_target`

Earlier versions of this action ran on `pull_request_target` with a personal access token.
This version fails on any trigger other than `push`.

To migrate:

1. Replace the `on:` block with the `push` trigger from the example above.
2. Remove `github.event.pull_request.merged == true` from the job's `if:`.
3. Add the `permissions` blocks from the example.
4. Set `token: ${{ github.token }}`.
5. Delete the `MILESTONE_LABELER_TOKEN` repository secret.
