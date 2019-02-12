from json import load
from os.path import join
from os.path import abspath
from os.path import dirname

# SCOPES
SCOPES = ['https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/documents']

# SECRETS
secrets_path = join(dirname(dirname(abspath(__file__))), 'secrets')
TOKENS_FILE_PATH = join(secrets_path, 'token.pickle')
CREDS_FILE_PATH = join(secrets_path, 'client_id.json')
CONFIG_FILE_PATH = join(secrets_path, 'config.json')

# CONFIGS
with open(CONFIG_FILE_PATH, 'r') as f:
    data = load(f)
    LLT_NOTES_DIR = data['llt_notes_dir']
