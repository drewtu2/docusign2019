import os
import base64
from docusign_esign import *
from docusign_esign.rest import ApiException

class DocusSignConfig():
    def __init__(self):
        self.access_token = os.environ["DOCUSIGN_OAUTH"]
        self.account_id = os.environ["APIAccountId"]
        self.signer_name = None
        self.signer_email = None
        self.cc_email = "tu.a+congressman@husky.neu.edu"
        self.cc_name = "congress man bill"
        self.file_name_path = None
        self.base_url = None
        self.client_user_id = '123'
        self.authentication_method = None
        self.api_base_path = 'https://demo.docusign.net/restapi'
        self.APP_PATH = os.path.dirname(os.path.abspath(__file__))

    def set_signer_name(self, name: str):
        self.signer_name = name 
        return self
    
    def set_signer_email(self, email: str):
        self.signer_email = email
        return self

    def set_file_name_path(self, path: str):
        self.file_name_path = path
        return self
    
    def set_base_url(self, url: str):
        self.base_url = url
        return self
    
    def set_cc_email(self, email: str):
        self.cc_email = email
        return self

    def set_cc_name(self, name: str):
        self.cc_name = name 
        return self
    
    def build(self):
        return self
    
class DocuSigner():
    
    def __init__(self, config):
        # Settings
        # Fill in these constants
        #
        # Obtain an OAuth access token from https://developers.hqtest.tst/oauth-token-generator
        self.access_token = config.access_token
        # Obtain your accountId from demo.docusign.com -- the account id is shown in the drop down on the
        # upper right corner of the screen by your picture or the default picture. 
        self.account_id = config.account_id

        # Recipient Information:
        self.signer_name = config.signer_name
        self.signer_email = config.signer_email
        self.client_user_id = config.client_user_id # Used to indicate that the signer will use an embedded
                               # Signing Ceremony. Represents the signer's userId within
                               # your application.

        self.cc_email = config.cc_email
        self.cc_name = config.cc_name

        # The document you wish to send. Path is relative to the root directory of this repo.
        # file_name_path = 'demo_documents/World_Wide_Corp_lorem.pdf'
        self.file_name_path = config.file_name_path

        # The url of this web application
        self.base_url = config.base_url

        self.authentication_method = 'None' # How is this application authenticating
                                       # the signer? See the `authenticationMethod' definition
                                       # https://developers.docusign.com/esign-rest-api/reference/Envelopes/EnvelopeViews/createRecipient

        # The API base_path
        self.api_base_path = config.api_base_path

        # Constants
        self.APP_PATH = config.APP_PATH

    def embedded_signing_ceremony(self):
        """
        The document <file_name> will be signed by <signer_name> via an
        embedded signing ceremony.
        """
        #
        # Step 1. The envelope definition is created.
        #         One signHere tab is added.
        #         The document path supplied is relative to the working directory
        #
        # Create the component objects for the envelope definition...
        with open(os.path.join(self.APP_PATH, self.file_name_path), "rb") as file:
            content_bytes = file.read()
        base64_file_content = base64.b64encode(content_bytes).decode('ascii')

        document = Document( # create the DocuSign document object 
            document_base64 = base64_file_content, 
            name = 'Example document', # can be different from actual file name
            file_extension = 'pdf', # many different document types are accepted
            document_id = 1 # a label used to reference the doc
        )

        # Create the signer recipient model 
        signer = Signer( # The signer
            email = self.signer_email, 
            name = self.signer_name, 
            recipient_id = "1", 
            routing_order = "1",
            client_user_id = self.client_user_id, # Setting the client_user_id marks the signer as embedded
        )
        # Create the cc person (senator)
        cc1 = CarbonCopy(email=self.cc_email, name=self.cc_name, \
            recipient_id="2", routing_order="2")


        sign_here = SignHere( # DocuSign SignHere field/tab
            document_id = '1', 
            page_number = '1', 
            recipient_id = '1', 
            tab_label = 'SignHereTab',
            anchor_string= "Your Constituent",
            anchor_x_offset="1",
            anchor_y_offset="1",
            anchor_units="inches",
            anchor_ignore_if_not_present="false",
            anchor_case_sensitive="false")

        # Add the tabs model (including the sign_here tab) to the signer
        signer.tabs = Tabs(sign_here_tabs = [sign_here]) # The Tabs object wants arrays of the different field/tab types

        # Next, create the top level envelope definition and populate it.
        envelope_definition = EnvelopeDefinition(
            email_subject = "Please sign this document sent from the Python SDK",
            documents = [document], # The order in the docs array determines the order in the envelope
            recipients = Recipients(signers = [signer]), # The Recipients object wants arrays for each recipient type
            status = "sent" # requests that the envelope be created and sent.
        )

        #
        #  Step 2. Create/send the envelope.
        #
        api_client = ApiClient()
        api_client.host = self.api_base_path
        api_client.set_default_header("Authorization", "Bearer " + self.access_token)

        envelope_api = EnvelopesApi(api_client)
        results = envelope_api.create_envelope(self.account_id, envelope_definition=envelope_definition)

        #
        # Step 3. The envelope has been created.
        #         Request a Recipient View URL (the Signing Ceremony URL)
        #
        envelope_id = results.envelope_id
        recipient_view_request = RecipientViewRequest(
            authentication_method = self.authentication_method, client_user_id = self.client_user_id,
            recipient_id = '1', return_url = self.base_url + '/dsreturn',
            user_name = self.signer_name, email = self.signer_email
        )

        results = envelope_api.create_recipient_view(self.account_id, envelope_id,
            recipient_view_request = recipient_view_request)

        #
        # Step 4. The Recipient View URL (the Signing Ceremony URL) has been received.
        #         Redirect the user's browser to it.
        #
        return results.url

if __name__ == "__main__":
    config = DocusSignConfig()
    config.set_base_url("localhost:5000")
    config.set_file_name_path("sample_letter/sample_letter.pdf")
    config.set_signer_name("Bob the Builder")
    config.set_signer_email("Bob@gmail.com")

    signer = DocuSigner(config)
    redirect = signer.embedded_signing_ceremony()