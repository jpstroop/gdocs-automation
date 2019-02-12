# Google Docs Automation

To get started:

* Create a project and enable the Google Docs API:
  1. Create a project: https://console.cloud.google.com/cloud-resource-manager
  2. Visit https://console.developers.google.com/apis/api/drive.googleapis.comoverview and enable the Drive API
  3. If there are creds available, download `mv` them to `secrets/credentials.json`
  4. Otherwise, Click "CREATE CREDENTIALS":
     a. Which API are you using? Choose "Google Drive API"
     b. Where will you be calling the API from? Choose "Other UI (e.g. Windows, CLI tool)"
     c. What data will you be accessing? Choose "User Data"
     d. Follow remaining instructions
     e. Download** credentials and place them in `secrets/credentials.json` (Note that the name of the downloaded file may be different. It's the contents that are important. `mv` the file to the path/name above.)
* Place a JSON file `config.json` in `secrets/` with the following keys:
    ```json
    {
      "tbd_1" : "foo",
      "tbd_2" : ["bar", "baz", "quux"]
    }
    ```
