# File 1
# Update the path of the input file line 8
# Update the path of the output file line 18 **do not change /%s.pdf**
# `pip install pdfquery PyPDF2` **run this command in the terminal**
# Run the code

from PyPDF2 import PdfWriter, PdfReader
import pdfquery

inp = ''
inputpdf = PdfReader(open(inp, "rb"))

for i in range(len(inputpdf.pages)):
    qpdf = pdfquery.PDFQuery(inp)
    qpdf.load(i)
    id = qpdf.pq(
        'LTTextLineHorizontal:in_bbox("137.28, 136.75, 185.87, 146.75")').text()
    res = id.strip().strip('-').strip()

    output = PdfWriter()
    output.add_page(inputpdf.pages[i])
    res = res.replace("/", "_")
    with open("/%s.pdf" % res, "wb") as outputStream:
        output.write(outputStream)
