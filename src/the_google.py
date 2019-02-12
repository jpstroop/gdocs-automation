from constants import CREDS_FILE_PATH
from constants import SCOPES
from constants import TOKENS_FILE_PATH
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.exceptions import RefreshError
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from os.path import exists
import pickle

class GoogleService():
    def __init__(self):
        self._creds = None

    @property
    def creds(self):
        if self._creds is None:
            if exists(TOKENS_FILE_PATH):
                with open(TOKENS_FILE_PATH, 'rb') as token:
                    self._creds = pickle.load(token)
            try:
                if not self._creds or not self._creds.valid:
                    if self._creds and self._creds.expired and self._creds.refresh_token:
                        self._creds.refresh(Request())
                    else:
                        flow = InstalledAppFlow.from_client_secrets_file(CREDS_FILE_PATH, SCOPES)
                        self._creds = flow.run_local_server()
                    with open(TOKENS_FILE_PATH, 'wb') as token:
                        pickle.dump(self._creds, token)
            except RefreshError as re:
                exit('Token is likely missing or stale. See README.md')
        return self._creds

class GoogleDocs(GoogleService):
    def __init__(self):
        super().__init__()
        self._service = None

    @property
    def service(self):
        if self._service is None:
            self._service = build('docs', 'v1', credentials=self.creds)
        return self._service

class GoogleDrive(GoogleService):
    def __init__(self):
        super().__init__()
        self._service = None

    @property
    def service(self):
        if self._service is None:
            self._service = build('drive', 'v3', credentials=self.creds)
        return self._service


    def ls(self, page_size=25, page_token=None, query=None, v=False):
        '''Example queries:
        https://developers.google.com/drive/api/v3/search-parameters#examples_for_fileslist
        Fields:
        https://developers.google.com/resources/api-libraries/documentation/drive/v3/python/latest/drive_v3.files.html#list
        '''
        fields = 'nextPageToken, files(name, originalFilename, createdTime, modifiedTime, id, parents)'
        files = self.drive_service.files()

        results = files.list(
            q=query,
            pageSize=page_size,
            fields=fields, pageToken=page_token).execute()
        items = results.get('files', [])
        next_page_token = results.get('nextPageToken')
        if not items:
            return None
        else:
            items = list(map(Drive.format, items))
            return (next_page_token, items)

    def touch(self, name, parent_id, v=False):
        'Create a file'
        pass

    def mkdir(self, name, parent_id, p=False, v=False):
        '''Create a directory. If p=True and name is a list, create intermediate
        directories as necessary.'''
        pass

    def rm(self, id): # should this take a query?
        pass

    # What else?
