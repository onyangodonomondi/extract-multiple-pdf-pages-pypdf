import PyPDF2
pdffileObj = open("psc.pdf", "rb")
pdfreader = PyPDF2.PdfFileReader(pdffileObj)
print(pdfreader.numPages)
pageobj=pdfreader.getPage(0)
data=pageobj.extractText()
print(data)