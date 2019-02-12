from json import load
from os.path import join
from os.path import abspath
from os.path import dirname
# SCOPES
# SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']
SCOPES = ['https://www.googleapis.com/auth/drive']
# SECRETS
secrets_path = join(dirname(dirname(abspath(__file__))), 'secrets')
TOKENS_FILE_PATH = join(secrets_path, 'token.pickle')
CREDS_FILE_PATH = join(secrets_path, 'credentials.json')
CONFIG_FILE_PATH = join(secrets_path, 'config.json')

# CONFIGS
with open(CONFIG_FILE_PATH, 'r') as f:
    data = load(f)
    PHOTOS_FOLDER_ID = data['photos_folder_id']
