# Github permissions management through ansible

This repository manages the GitHub permissions for the osism organization.
Based on https://github.com/opentelekomcloud-infra/gitstyring.

### Usage:
```sh
export GITHUB_TOKEN="<github-token>"
export GITHUB_USER="<github-username>"
cd github-permissions
ansible-playbook playbooks/run.yml -e github_repos_state=present -e root_dir="../../orgs"
```
