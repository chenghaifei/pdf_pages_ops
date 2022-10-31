
"""
this script delete pages number specified in delete_page_index from pdf1 file.
page index start from 1, not 0.

2022-10-30, Haifei Cheng, initial version 
"""

from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter


pdf1 = PdfFileReader("sample1.pdf")
delete_page_index = [2,4]

pdf_writer = PdfFileWriter()

idx = 1
for page in pdf1.pages:
    if idx not in delete_page_index:
        pdf_writer.addPage(page)
    idx = idx + 1

# generate output pdf file
with Path("output.pdf").open(mode="wb") as output_file:
    pdf_writer.write(output_file)

