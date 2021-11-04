# GitHub repository management through Ansible & Python

This repository manages the GitHub repositories for the OSISM organization.

## Installation

```sh
ansible-galaxy collection install ansible-collection-gitcontrol
```

## Usage

As a prerequisite, a PAT must be created. The rights ``repo`` and ``admin:org`` are required.

```sh
export GITHUB_TOKEN="<github-token>"
ansible-playbook playbook.yaml -e github_token=$GITHUB_TOKEN
```
