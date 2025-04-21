# File 1
# Update the path of the input file line 8
# Update the path of the output file line 18 **do not change /%s.pdf**
# `pip install pdfquery PyPDF2` **run this command in the terminal**
# Run the code

from PyPDF2 import PdfWriter, PdfReader
import pdfquery

inp = './2025/Batch1/1.pdf'
inputpdf = PdfReader(open(inp, "rb"))

for i in range(len(inputpdf.pages)):
    qpdf = pdfquery.PDFQuery(inp)
    qpdf.load(i)
    id = qpdf.pq(
        'LTTextLineHorizontal:in_bbox("137.93, 137.518, 186.399, 147.478")').text()
    # 137.93, 137.518, 186.399, 147.478
    res = id.strip().strip('-').strip()

    output = PdfWriter()
    output.add_page(inputpdf.pages[i])
    res = res.replace("/", "_")
    with open("./2025/Batch1/%s.pdf" % res, "wb") as outputStream:
        output.write(outputStream)
