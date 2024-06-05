import pdfplumber
import pdfquery




# path = './PDF/ppp.pdf'
# with pdfplumber.open(path) as pdf:
#     for  page  in pdf.pages:
#         print(page.extract_text())
        

pdf = pdfquery.PDFQuery('./PDF/ppp.pdf')
pdf.load()


#convert the pdf to XML
pdf.tree.write('./PDF/TestXML.xml', pretty_print = True)


# LTTextBoxHorizontal
# 176.2, 254.55, 226.973, 265.55