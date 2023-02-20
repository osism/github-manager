# copied from https://github.com/SovereignCloudStack/
# github-manager/blob/main/check_repositories.py
# thanks @itrich!
import github
import os
import sys
import yaml

API_TOKEN = os.environ.get("API_TOKEN")
ORGANIZATION = os.environ.get("ORGANIZATION", "osism")

gh = github.Github(login_or_token=API_TOKEN)

existing_repos = set()
defined_repos = set()
error = 0

for repo in gh.get_organization(ORGANIZATION).get_repos(visibility="public"):
    existing_repos.add(repo.name)

repositories_dir = os.path.join("orgs/" + ORGANIZATION + "/repositories")

for filename in os.listdir(repositories_dir):
    if filename.endswith('.yaml') or filename.endswith('.yml'):
        with open(os.path.join(repositories_dir, filename)) as f:
            yaml_data = yaml.safe_load(f)
            if yaml_data is not None:
                defined_repos.add(list(yaml_data.keys())[0])

not_on_github = defined_repos.difference(existing_repos)
not_defined = existing_repos.difference(defined_repos)

if (len(not_on_github) != 0):
    print(f"Not on GitHub: {not_on_github}", file=sys.stderr)
    error += 1

if (len(not_defined) != 0):
    print(f"Not defined in github-manager: {not_defined}", file=sys.stderr)
    error += 1

sys.exit(error)
