# coding: utf8

import os
from CustomPDF import CustomPDF
from Entities import *
from DatabaseGateway import DatabaseGateway
 
class LetterBuilder:

    APP_PATH = os.path.dirname(os.path.abspath(__file__))
    DEFAULT_LETTER_FILE= os.path.join(APP_PATH, 'sample_letter/build/temp.pdf')

    def __init__(self):
        self.recipient = None 
        self.sender = None
        self.dbGateway = DatabaseGateway()
        self.issue = "issue1"
        self.pdf_path = self.DEFAULT_LETTER_FILE

    def set_recipient(self, input: Person):
        self.recipient = input
        return self 
    
    def set_sender(self, input: PersonWithId):
        self.sender = input
        return self 

    def set_db(self, input: DatabaseGateway):
        self.dbGateway = input
        return self 
    
    def set_issue(self, input: str):
        self.issue = input
        return self 
    
    def set_pdf_path(self, input: str):
        self.pdf_path = input
        return self 
    
    def build(self):
        '''
        Creates a pdf for a given issue 
        '''
        
        print("Building pdf")
        pdf = CustomPDF()
        pdf.config(self.sender.person, self.recipient, self._get_message_content())
        pdf.build(self.pdf_path)

        return self.pdf_path

    def _get_message_content(self):
        """
        issue should be issue1, issue2, issue3
        """
        message =  "Dear " + str(self.recipient) + ",\n" \
            + self.dbGateway.get_issue_body(self.issue) \
            + "\n \n" \
            + "Your Constituent, \n\n\n\n" \
            + str(self.sender.person) \
            + "\n" \
            + str(self.sender.person.address) \
            + "\n \n" \
            + self._load_history()
        
        return message
    
    def _load_history(self) -> str: 
        text = "For reference of my involvment in our National Parks, I have visted the following parks.\n"
        for entry in self.dbGateway.get_park_history_from_userId(self.sender.id):
            text += str(entry)
        return text

if __name__ == '__main__':
    bob = PersonWithId(Person("Bob", "Builder", 
        Address("101 bob way", "bob town", "bb", "00000"),
        "bob@gmail.com"), "000")

    sen = Person("sob", "suilder", 
        Address("101 sob way", "sob town", "ss", "10000"),
        "sob@gmail.com")

    test_file = os.path.join(LetterBuilder.APP_PATH, "sample_letter/build/test.pdf")
    
    test = LetterBuilder() \
        .set_recipient(sen) \
        .set_sender(bob) \
        .set_db(DatabaseGateway()) \
        .set_issue("issue1") \
        .set_pdf_path(test_file) \
        .build()

    print(test)