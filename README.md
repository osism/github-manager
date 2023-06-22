# GitHub repository management through Ansible & Python

This repository manages the GitHub repositories for the OSISM organization.

## Installation

```sh
pipenv install
pipenv shell
ansible-galaxy collection install ansible-collection-gitcontrol
```

## Prerequisite

A fine-grained personal access token (https://github.com/settings/tokens?type=beta)
must be created with the following permissions:

* Organization permissions: Read and Write access to custom repository roles,
  members, organization administration, organization announcement banners, and
  organization projects
* Repository permissions: Read access to metadata, Read and Write access to
  administration, code, and issues

## Usage

```sh
export GITHUB_TOKEN="<github-token>"
ansible-playbook -i localhost, playbook.yaml
```

Set ``-e log=true`` to enable logging output.

## Limitiations

* It is not possible to add already created, but still empty, repositories here.
  Before this is possible, at least one commit must have been made on the main
  branch.
* Only the owner of the organization should currently merge pull requests. The
  token in the github action would not work if someone else triggers it.

## Github Actions

For the Github Action workflows a repository secret ``GHP`` is provided. This had
only a short validity and must be renewed regularly.

If the following error in the logs comes from ``Manage github repositories`` the
token has expired and must be renewed OR someone different than the owner merged
a pull request.

```
PLAY [localhost] ***************************************************************

TASK [Gathering Facts] *********************************************************
ok: [localhost]

TASK [manage repositories] *****************************************************
fatal: [localhost]: FAILED! => {"censored": "the output has been hidden due to the fact that 'no_log: true' was specified for this result", "changed": false}

PLAY RECAP *********************************************************************
localhost                  : ok=1    changed=0    unreachable=0    failed=1    skipped=0    rescued=0    ignored=0

```
