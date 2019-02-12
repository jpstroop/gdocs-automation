from the_google import GoogleDocs

DOCUMENT_ID = '195j9eDD3ccgjQRttHhJPymLJUCOUjs-jmwTrekvdjFE'

if __name__ == '__main__':
    docs_api = GoogleDocs()
    document = docs_api.service.documents().get(documentId=DOCUMENT_ID).execute()
    print('The title of the document is: {}'.format(document.get('title')))
