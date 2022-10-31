# this script combine two pdf files, put pdf2 to the end of pdf1.
"""
2022-10-30, Haifei Cheng, initial version 
"""

from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter


pdf1 = PdfFileReader("sample1.pdf")
pdf2 = PdfFileReader("sampleone.pdf")

pdf_writer = PdfFileWriter()

for page in pdf1.pages:
    pdf_writer.addPage(page)
    
for page in pdf2.pages:
    pdf_writer.addPage(page)
    
# generate output pdf file
with Path("output.pdf").open(mode="wb") as output_file:
    pdf_writer.write(output_file)

