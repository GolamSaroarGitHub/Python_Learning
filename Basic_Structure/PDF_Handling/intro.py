import PyPDF2

pdfFileObj=open('tkinter.pdf','rb')
pdfReader=PyPDF2.PdfFileReader(pdfFileObj)

print(pdfReader.numPages)

pageObj=pdfReader.getPage(15)
print(pageObj.extractText())
# pageObj.extractText()