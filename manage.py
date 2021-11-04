import os
import github
import logging
import yaml

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S')

GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
ORGANIZATION = os.environ.get("ORGANIZATION", "osism")

gh = github.Github(login_or_token=GITHUB_TOKEN)

with open("config.yaml") as fp:
    CONFIG = yaml.load(fp, Loader=yaml.SafeLoader)

for gh_repository in gh.get_organization(ORGANIZATION).get_repos(type='public'):

    if gh_repository.archived:
        continue

    logging.info(f"Checking {gh_repository.name}")

    # handle labels

    gh_labels = gh_repository.get_labels()
    
    labels = {}

    for gh_label in gh_labels:
        labels[gh_label.name] = gh_label

    for label in CONFIG['labels']:
        if label['name'] not in labels.keys():
            logging.info(f"{gh_repository.name} - label {label['name']} does not exist")
            gh_repository.create_label(
                name=label['name'],
                description=label['description'],
                color=label['color']
            )
        else:
            
            gh_label = labels[label['name']]

            if gh_label.description != label['description'] or gh_label.color != label['color']:
                logging.info(f"{gh_repository.name} - label {label['name']} changed")
                gh_label.edit(name=label['name'], description=label['description'], color=label['color'])

            del labels[label['name']]

    # remove undefined labels

    for label in labels.keys():
        logging.info(f"{gh_repository.name} - {label} should not exist")
        gh_label = labels[label]
        gh_label.delete()

    # handle milestones

    gh_milestones = gh_repository.get_milestones(state='open')

    milestones = []
    current_milestone = CONFIG['current_milestone']
    next_milestone = CONFIG['next_milestone']

    for gh_milestone in gh_milestones:
        milestones.append(gh_milestone.title)
        if gh_milestone.title not in [current_milestone, next_milestone]:
            logging.info(f"{gh_repository.name} - {gh_milestone.title} should be in state 'closed'")
            gh_milestone.edit(title=gh_milestone.title, state="closed")

    if current_milestone not in milestones:
        logging.info(f"{gh_repository.name} - current milestone {current_milestone} does not exist")
        gh_repository.create_milestone(title=current_milestone, state="open")

    if next_milestone not in milestones:
        logging.info(f"{gh_repository.name} - next milestone {next_milestone} does not exist")
        gh_repository.create_milestone(title=next_milestone, state="open")