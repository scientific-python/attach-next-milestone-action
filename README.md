# Attach Next Milestone

This action attaches the next open milestone to a given PR, if that PR
was merged.

A typical job would look like this:

```yaml
# .github/workflows/label-merged-prs.yaml

on:
  pull_request:
    types:
      - closed

jobs:
  milestone_pr:
    name: Milestone PR
    runs-on: ubuntu-latest
    steps:
      - uses: stefanv/attach-next-milestone@main
        with:
          token: ${{ secrets.MILESTONE_LABELER_TOKEN }}
```

To use the above, you will need to set a repository secret
`MILESTONE_LABELER_TOKEN` to a [personal access
token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)
that has permissions to modify PRs. You can generate these at https://github.com/settings/apps.

Permissions needed: `public_repo`.
