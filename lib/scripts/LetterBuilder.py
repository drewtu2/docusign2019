# coding: utf8

from CustomPDF import *
from Entities import *
import os
 
class LetterBuilder:

    def __init__(self):
        self.recipient = None
        self.sender = None
        self.park_history = [] 
        
        self.APP_PATH = os.path.dirname(os.path.abspath(__file__))
        self.issues = {
            "issue1": "sample_letter/issues/issue1.txt",
            "issue2": "sample_letter/issues/issue2.txt",
            "issue3": "sample_letter/issues/issue3.txt"
        }
    
    def set_recipient(self, person: Person):
        self.recipient = person
    
    def set_sender(self, person: Person):
        self.sender = person 

    def set_park_history(self, history):
        self.park_history = history

    def build(self, issue="issue1"):
        """
        issue should be issue1, issue2, issue3
        """
        message =  "Dear " + str(self.recipient) + ",\n" \
            + self.load_issue(issue) \
            + "\n \n" \
            + "Your Constituent, \n\n\n\n" \
            + str(self.sender) \
            + "\n" \
            + str(self.sender.address) \
            + "\n \n" \
            + self.load_history()
        
        return message

    def load_issue(self, issue):
        with open(os.path.join(self.APP_PATH, self.issues[issue])) as f:
            text = f.read()
        return text
    
    def load_history(self):
        text = ""
        for entry in self.park_history:
            text += str(entry)
        return text

    def create_pdf(self, pdf_path, issue="issue1"):
        print("Building pdf")
        pdf = CustomPDF()
        pdf.config(self.sender, self.recipient, "hello")
        # Create the special value {nb}
        pdf.alias_nb_pages()
        pdf.add_page()
        pdf.add_font('DejaVu', '', os.path.join(self.APP_PATH, 'DejaVuSansCondensed.ttf'), uni=True)
        pdf.set_font('DejaVu', '', 14)
        line_no = 1
        
        pdf.multi_cell(0, 10, txt=self.build(issue))

        pdf.output(pdf_path)

if __name__ == '__main__':
    test = LetterBuilder()
    #test.create_pdf('header_footer.pdf')
    bob = Person("Bob", "Builder", 
        Address("101 bob way", "bob town", "bb", "00000"),
        "bob@gmail.com")
    sen = Person("sob", "suilder", 
        Address("101 sob way", "sob town", "ss", "10000"),
        "sob@gmail.com")
    test.set_recipient(sen)
    test.set_sender(bob)
    test.set_park_history([ParkHistoryEntry("Yellow Stone National Park", "Jan 1, 2019")])
    print(test.build("issue1"))
    print(test.build("issue2"))
    print(test.build("issue3"))
    
    test.create_pdf('header_footer.pdf', "issue1")