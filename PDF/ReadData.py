import pandas as pd
import pdfquery
import glob




files = glob.glob("./PDF/Test.pdf")

for file in files:
    pdf = pdfquery.PDFQuery(file)
    pdf.load(0)


#convert the pdf to XML
    id = pdf.pq('LTTextBoxHorizontal:in_bbox("176.2, 254.55, 226.973, 265.55")').text()
    res = id.strip().strip('-').strip()
    print(res)

