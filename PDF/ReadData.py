import pandas as pd
import pdfquery
import glob

files = glob.glob("./test/**")

for file in files:
    pdf = pdfquery.PDFQuery(file)
    pdf.load(0)


#convert the pdf to XML
    id = pdf.pq('LTTextLineHorizontal:in_bbox("137.93, 137.518, 186.399, 147.478")').text()
    res = id.strip().strip('-').strip()
    print(res)

