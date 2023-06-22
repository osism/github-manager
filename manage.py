import os
import github
import logging
import yaml
from argparse import ArgumentParser

logging.basicConfig(
    format="%(asctime)s - %(message)s", level=logging.INFO, datefmt="%Y-%m-%d %H:%M:%S"
)

GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
ORGANIZATION = os.environ.get("ORGANIZATION", "osism")

gh = github.Github(login_or_token=GITHUB_TOKEN)

parser = ArgumentParser()
parser.add_argument(
    "-d", "--dry", default=False, help="Dry run - if true does not change github items"
)
args = parser.parse_args()

with open("config.yaml") as fp:
    CONFIG = yaml.load(fp, Loader=yaml.SafeLoader)

for gh_repository in gh.get_organization(ORGANIZATION).get_repos(type="public"):

    if gh_repository.archived:
        continue

    logging.info(f"Checking {gh_repository.name}")

    # handle labels

    gh_labels = gh_repository.get_labels()

    labels = {}

    for gh_label in gh_labels:
        labels[gh_label.name] = gh_label

    for label in CONFIG["labels"]:
        if label["name"] not in labels.keys():
            logging.info(f"{gh_repository.name} - label {label['name']} does not exist")
            if args.dry is False:
                try:
                    gh_repository.create_label(
                        name=label["name"],
                        description=label["description"],
                        color=label["color"],
                    )
                except:
                    logging.info(
                        f"{gh_repository.name} - label {label['name']} - Failed to create label"
                    )
        else:
            gh_label = labels[label["name"]]

            if (
                gh_label.description != label["description"]
                or gh_label.color != label["color"]
            ):
                logging.info(f"{gh_repository.name} - label {label['name']} changed")
                if args.dry is False:
                    gh_label.edit(
                        name=label["name"],
                        description=label["description"],
                        color=label["color"],
                    )

            del labels[label["name"]]

    # remove undefined labels

    for label in labels.keys():
        logging.info(f"{gh_repository.name} - {label} should not exist")
        if args.dry is False:
            gh_label = labels[label]
            gh_label.delete()
            logging.info(f"{gh_repository.name} - {label} removed")
