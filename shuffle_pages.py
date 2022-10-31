
"""
this script sort pages in specified order.
page index start from 1, not 0.

2022-10-30, Haifei Cheng, initial version 
"""

from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter

pdf1 = PdfFileReader("sample1.pdf")
page_order = [4,5,1,2,3]

all_page = []
for page in pdf1.pages:
    all_page.append(page)

pdf_writer = PdfFileWriter()

for idx in page_order:
    idx0 = idx - 1;
    pdf_writer.addPage(all_page[idx0])

# generate output pdf file
with Path("output.pdf").open(mode="wb") as output_file:
    pdf_writer.write(output_file)

