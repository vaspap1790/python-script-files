import json

with open('config.json') as f:
    config = json.load(f)

# You need to add the following keys to a config.json file:
PROJECT_DIR = config.get('PROJECT_DIR')
DIRECTORIES = config.get('DIRECTORIES')
FILES_TO_COPY_DIR = config.get('FILES_TO_COPY_DIR')