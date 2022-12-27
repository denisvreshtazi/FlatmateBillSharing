from bill import Bill
from flatmate import Flatmate
from pdfReport import PdfReport

bill_amount = float(input("What is the total bill amount? "))
period = input("What is the bill's period? ")

# First flatmate data
flatmate1_name = input("What is the name of the first flatmate? ")
flatmate1_days = int(input(f"What is the total number of days of {flatmate1_name}? "))

# Second flatmate data
flatmate2_name = input("What is the name of the second flatmate? ")
flatmate2_days = int(input(f"What is the total number of days of {flatmate2_name}? "))

bill = Bill(bill_amount, period)
flat1 = Flatmate(flatmate1_name, flatmate1_days)
flat2 = Flatmate(flatmate2_name, flatmate2_days)

print(f"{flat1.name} pays: ", flat1.pays(bill, flat2))
print(f"{flat2.name} pays: ", flat2.pays(bill, flat1))

pd = PdfReport(filename=f'{bill.period.replace(" ", "")}.pdf')
pd.generate(flat1, flat2, bill)
