# GitHub repository management through Ansible & Python

This repository manages the GitHub repositories for the OSISM organization.

## Installation

```sh
pipenv install
pipenv shell
ansible-galaxy collection install ansible-collection-gitcontrol
```

## Usage

As a prerequisite, a PAT must be created. The rights ``repo`` and ``admin:org`` are required.

```sh
export GITHUB_TOKEN="<github-token>"
ansible-playbook playbook.yaml -e github_token=$GITHUB_TOKEN
```

## Limitiations

It is not possible to add already created, but still empty, repositories here. Before this is possible,
at least one commit must have been made on the main branch.

## Github Actions

For the Github Action workflows a repository secret ``GHP`` is provided. This had only a short
validity and must be renewed regularly.

If the following error in the logs comes from ``Manage github repositories``x the token has
expired and must be renewed.

```
Run pipenv run ansible-playbook playbook.yaml -e github_token=$GITHUB_TOKEN
Warning: : No inventory was parsed, only implicit localhost is available
Warning: : provided hosts list is empty, only localhost is available. Note that
the implicit localhost does not match 'all'

PLAY [localhost] ***************************************************************

TASK [Gathering Facts] *********************************************************
ok: [localhost]

TASK [manage repositories] *****************************************************
fatal: [localhost]: FAILED! => {"censored": "the output has been hidden due to the fact that 'no_log: true' was specified for this result", "changed": false}

PLAY RECAP *********************************************************************
localhost                  : ok=1    changed=0    unreachable=0    failed=1    skipped=0    rescued=0    ignored=0

```
