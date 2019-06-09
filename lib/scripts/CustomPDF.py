from fpdf import FPDF
from Entities import *
import os

class CustomPDF(FPDF):

    def config(self, sender: Person, recipient: Person, text):
        self.sender = sender
        self.recipient = recipient
        self.text = text
        self.APP_PATH = os.path.dirname(os.path.abspath(__file__))
 
    def build(self, pdf_path: str):
        print("Building pdf to %s" % pdf_path)
        print("This usually takes a couple of seconds....")
        # Create the special value {nb}
        self.alias_nb_pages()
        self.add_page()
        self.add_font('DejaVu', '', os.path.join(self.APP_PATH, 'DejaVuSansCondensed.ttf'), uni=True)
        self.set_font('DejaVu', '', 14)
        
        self.multi_cell(0, 10, txt=self.text)
        self.output(pdf_path)

    def header(self):
        # Set up a logo
        self.image(os.path.join(self.APP_PATH, 'sample_letter/recycle.png'), 10, 8, 33)
        self.set_font('Arial', 'B', 15)
 
        # Add an address
        self.cell(100)
        self.cell(0, 5, "%s %s"%(self.sender.first, self.sender.last), ln=1)
        self.cell(100)
        self.cell(0, 5, self.sender.address.street, ln=1)
        self.cell(100)
        self.cell(0, 5, "(%s, %s)"%(self.sender.address.city, self.sender.address.state), ln=1)
 
        # Line break
        self.ln(20)
 
    def footer(self):
        self.set_y(-10)
 
        self.set_font('Arial', 'I', 8)
 
        # Add a page number
        page = 'Page ' + str(self.page_no()) + '/{nb}'
        self.cell(0, 10, page, 0, 0, 'C')