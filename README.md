# GitHub permissions management through Ansible

This repository manages the GitHub permissions for the OSISM organization.

Based on https://github.com/opentelekomcloud-infra/gitstyring.

## Usage

```sh
export GITHUB_TOKEN="<github-token>"
export GITHUB_USER="<github-username>"
export GITSTYRING_ROOT_DIR="../../orgs"
cd gitstyring
ansible-playbook playbooks/run.yml -e github_repos_state=present
```
