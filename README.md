# Google Docs Automation

A set of helpful functions for automating tasks in Google Drive and Google Docs. [WIP]

[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-372/) [![MIT License](https://img.shields.io/badge/license-MIT-000.svg)](https://opensource.org/licenses/MIT)


To get started:

1. Make sure you have a working [pipenv](https://pipenv.readthedocs.io/en/latest/) environment, with Python 3.7. Clone and run `pipenv install`.
2. Create a project and enable the Google Docs API:
   1. Create a project: https://console.cloud.google.com/cloud-resource-manager
   2. Visit https://console.developers.google.com/apis/library/docs.googleapis.com and enable the Docs API
   3. If there are creds available, download `mv` them to `secrets/client_id.json`
   4. Otherwise, Click "CREATE CREDENTIALS":
      1. Which API are you using? Choose "Google Drive API"
      2. Where will you be calling the API from? Choose "Other UI (e.g. Windows, CLI tool)"
      3. What data will you be accessing? Choose "User Data"
      4. Follow remaining instructions
      5. Download** credentials and place them in `secrets/client_id.json` (Note that the name of the downloaded file may be different. It's the contents that are important. `mv` the file to the path/name above.)
3. Place a JSON file `config.json` in `secrets/` with the following keys:
    ```json
    {
      "tbd_1" : "foo",
      "tbd_2" : ["bar", "baz", "quux"]
    }
    ```
