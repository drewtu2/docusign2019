# Usage 
Install requirements file at root directory of project
`pip install -r requirements.txt`

Call ICareActivity
`python ICareActivity.py --userId=000 --issueId="issue1" --hostUrl="localhost:5000"`

- `userID`: for now, needs to be 000 since we only have 1 user
- `issueID`: issue1, issue2, issue3
- `hostUrl`: the root of the webserver. docusign will always attempt to redirect to 
`hostUrl/dsreturn`

**YOU NEED A DOCUSIGN OAUTH KEY FOR THIS TO WORK**
expects environmental variables to be set
- `DOCUSIGN_OAUTH= <DOCUSIGN KEY>`
- `APIAccountId= <DOCUSIGN ID>`
