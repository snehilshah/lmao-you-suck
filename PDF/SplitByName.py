from PyPDF2 import PdfWriter, PdfReader
import pdfquery


inp = 'PDF/Cards/M974_1001_Comm.pdf'
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
    with open("./PDF/Files/res/%s.pdf" % res, "wb") as outputStream:
        output.write(outputStream)
