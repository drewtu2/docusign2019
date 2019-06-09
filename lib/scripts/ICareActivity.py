import DocuSignInterface
from DatabaseGateway import *
from LetterBuilder import *

import argparse, sys

class ICareActivity:

    def __init__(self):
        self.APP_PATH = os.path.dirname(os.path.abspath(__file__))
        self.dbGateway = DatabaseGateway()
        self.letter = LetterBuilder()
        self.letter_file = os.path.join(self.APP_PATH, 'sample_letter/build/temp.pdf')


    def i_care(self, userId, issueId, callbackUrl="localhost:5000"):
        '''
        Main Entry point to submit a letter to a senator based on the issue 
        desired. 

        Returns the callback url given by docusign. 
        '''
        config = DocuSignInterface.DocusSignConfig()
        config.set_base_url(callbackUrl)

        config.set_file_name_path(self.generate_document(userId, issueId))
        config.set_signer_name(self.dbGateway.get_name_from_userId(userId))
        config.set_signer_email(self.dbGateway.get_email_from_userId(userId))

        signer = DocuSignInterface.DocuSigner(config)
        return signer.embedded_signing_ceremony()

    def generate_document(self, userId, issueId):
        '''
        Letter based off a template given by issueId. 
        Letter Customzized based off the personalized data from userId. 
        Pass CallbackUrl to docusign after sucessfull completion. 

        Returns file path with pdf
        '''
        self.letter.set_recipient(self.dbGateway.get_senator_from_userId(userId))
        self.letter.set_sender(self.dbGateway.get_person_from_userId(userId))
        self.letter.set_park_history(self.dbGateway.get_park_history_from_userId(userId))
    
        self.letter.create_pdf(self.letter_file, issueId)
        
        return self.letter_file

if __name__ == "__main__":

    parser=argparse.ArgumentParser()

    parser.add_argument('--userId', default="000", type=str, help='User id (000)')
    parser.add_argument('--issueId', default="issue1", type=str, help='IssueId ("issue1")')
    parser.add_argument('--hostUrl', default="localhost:5000", type=str, help='HostUrl ("localhost:5000")')
    args=parser.parse_args()

    activity = ICareActivity()
    return_url = activity.i_care(args.userId, args.issueId, args.hostUrl)
    
    print("Return Url: " + return_url)
