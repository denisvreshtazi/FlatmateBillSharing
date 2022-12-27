import webbrowser
from fpdf import FPDF
import os


class PdfReport:
    """
        Creates a pdf file that contains the report of the flatmates,
        their names, pays and the period.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Add logo
        # pdf.image("lHere goes the logo's path", w=40, h=40)

        # Add the title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt='Flatmates Bill', border=0, ln=1, align='C')

        # Insert period
        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=100, h=40, txt='Period: ', border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

        # Insert name and the amount of the flatmates
        pdf.set_font(family='Times', size=12)
        pdf.cell(w=100, h=25, txt=flatmate1.name, border=0)
        pdf.cell(w=150, h=25, txt=str(round(flatmate1.pays(bill, flatmate2), 2)), border=0, ln=1)

        pdf.cell(w=100, h=25, txt=flatmate2.name, border=0)
        pdf.cell(w=150, h=25, txt=str(round(flatmate2.pays(bill, flatmate1), 2)), border=0, ln=1)

        #  In case you wanted to change to a directory where you put the saved files, for example ..files/
        # os.chdir()

        pdf.output(self.filename)

        webbrowser.open(self.filename)
