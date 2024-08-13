'''*********************************************************************************************************************************
 * Name                 : script.py
 * Creation Date        : 25-05-2022
 * Last Modified        : 06-06-2022
----------------------------------------------------------------------------------------------------------------------------------
 * Author               : Badam Mayur Krishna
 * Author's Email       : mayurkrishna.b@alpha-numero.tech
----------------------------------------------------------------------------------------------------------------------------------
* Description           : Replacement of strings in xlsx file. 
**********************************************************************************************************************************'''

#importing fpdf module's FPDF
from fpdf import FPDF
#importing module PyPDF2 
import PyPDF2 


pdf = FPDF()
pdf.add_page()

pdf.set_font("Arial", 'I', size=11)

pdf.cell(30, 5, txt="Mayur krishna badam", ln=0, align='C')
pdf.cell(220, 5, txt="Date: 25/5/22", ln=1, align='C')
pdf.cell(30, 5, txt="Verification Engineer", ln=1, align='C')
pdf.cell(110, 5, txt="Skills: verilog, system verilog, UVM, python, linux,DOORs, synergy", ln=1, align='C')

pdf.output("resume.pdf")

#reading pdf
#opening file in read mode
file = open('resume.pdf', 'rb')

#accessing file using PyPDF2's method 
pdf_read = PyPDF2.PdfFileReader(file)
page = pdf_read.getPage(0)

#printing text by extracting text from the file
print(page.extractText())

#OUTPUT:
# Mayur krishna badam
# Date: 25/5/22
# Verification Engineer
# Skills: verilog, system verilog, UVM, python, linux,DOORs, synergy






#pdfobj = open('resume.pdf','rb')
#pdreader = PyPDF2.PdfFileReader(pdfobj)
#print (pdreader.numPages)
#page1 = pdreader.getPage(0)
#print(page1.extractText())
#pdfobj.close()
