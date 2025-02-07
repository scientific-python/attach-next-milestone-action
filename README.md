# Attach Next Milestone Action

This action attaches the next open milestone to merged PRs.

Currently, this action only looks at milestones that can be parsed as
version numbers.

A typical job would look like this:

```yaml
# .github/workflows/milestone-merged-prs.yaml

name: Milestone

on:
  pull_request_target:
    types:
      - closed
    branches:
      - 'main'

jobs:
  milestone_pr:
    name: attach to PR
    if: github.event.pull_request.merged == true
    runs-on: ubuntu-latest
    steps:
      - uses: scientific-python/attach-next-milestone-action@a4889cfde7d2578c1bc7400480d93910d2dd34f6
        with:
          token: ${{ secrets.MILESTONE_LABELER_TOKEN }}
```

To use the above, you will need to set a repository secret
`MILESTONE_LABELER_TOKEN` to a [fine-grained access token](https://github.blog/2022-10-18-introducing-fine-grained-personal-access-tokens-for-github/)
that has *read & write* permissions to modify *both* issues and PRs.
If you are generating a token for your org, you first need to enable fine-grained access tokens at
`https://github.com/organizations/<YOUR-ORGANIZATION>/settings/personal-access-tokens-onboarding`.

You can generate the token itself at https://github.com/settings/apps.

1. Personal access tokens -> Fine-grained tokens. Generate new token. Token name: milestone-labeler-token.
2. Select the org which owns the code repository.
   If you don't see your organization listed, you first need to
   [onboard it](https://github.com/organizations/<YOUR_ORG_NAME>/settings/personal-access-tokens-onboarding).
3. Choose "Only Select Repositories", and choose the correct one.
4. Permissions:
   - Repository Permissions -> Pull Requests -> Read and write.
   - Repository Permissions -> Issues -> Read and write.
6. Generate the token. If an error appears saying "Sorry, something went wrong", ignore it.

Copy the token, and navigate to your code repository. Under Settings
-> Secrets and variables -> Actions, add a repository secret named
`MILESTONE_LABELER_TOKEN`, and set its contents to the generated
token.

## Options

In the `with` clause, the following options are available:

- `force: true` : Overwrite existing milestones.

## Warning!

The workflow above runs as `pull_request_target`, meaning it has access to repository secrets.
This is not usually a problem, since our action does nothing but attach a milestone to a PR using the provided token.
But, you should **not add further commands to the workflow**, such as checking out the PR and executing code from it.
If you do that, PR authors can gain access to your secrets.
