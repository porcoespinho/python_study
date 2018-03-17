import os
import PyPDF2

path = "/Users/lvargas/Downloads/CONDUSEF_CC_stats"  # path to folder
page = 0  # page number to extract, index starts at 0 being page 1
writer = PyPDF2.PdfFileWriter()  # create PdfFileWriter object

# Iterate through all files in a folder using the os library’s listdir() method,
# which takes a path as the parameter and lists all files in that path
for pdf in os.listdir(path):
    PDFfilename = path + "/" + pdf
    pfr = PyPDF2.PdfFileReader(open(PDFfilename, "rb"))  # PdfFileReader object,
    # "rb" stands for "read bytes"
    pg0 = pfr.getPage(page)  # extract pg 1
    writer.addPage(pg0)  # add pg 1

NewPDFfilename = "allTables.pdf"  # filename of your PDF/directory where you want your new PDF to be
with open(NewPDFfilename, "wb") as outputStream:  # create new PDF
    writer.write(outputStream)  # write pages to new PDF
