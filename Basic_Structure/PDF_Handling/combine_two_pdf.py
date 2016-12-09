import PyPDF2

pdf1File=open('python_101.pdf','rb')
pdf2File=open('tkinter.pdf','rb')

pdf1Reader=PyPDF2.PdfFileReader(pdf1File)
pdf2Reader=PyPDF2.PdfFileReader(pdf2File)
pdfWriter=PyPDF2.PdfFileWriter()

for pageNum in range(pdf1Reader.numPages):
    pagObj=pdf1Reader.getPage(pageNum)
    pdfWriter.addPage(pagObj)

for pageNum in range(pdf2Reader.numPages):
    pagObj=pdf2Reader.getPage(pageNum)
    pdfWriter.addPage(pagObj)


pdfOututFile=open('CombinePdf.pdf','wb')
pdfWriter.write(pdfOututFile)
pdfOututFile.close()
pdf1File.close()
pdf2File.close()