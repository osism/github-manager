# GitHub permissions management through Ansible

This repository manages the GitHub permissions for the OSISM organization.

## Installation

```sh
ansible-galaxy collection install ansible-collection-gitcontrol
```

## Usage

```sh
export GITHUB_TOKEN="<github-token>"
ansible-playbook run.yaml -e github_token=$GITHUB_TOKEN
```
