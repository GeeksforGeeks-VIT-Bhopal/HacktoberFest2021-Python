import PyPDF2

pdfpath = input("Enter the name of your pdf file - please use backslash when typing in directory path: ")   
txtpath = input("Enter the name of your txt file - please use backslash when typing in directory path: ")

pdfobj = open(pdfpath, 'rb')

pdfread = PyPDF2.PdfFileReader(pdfobj)
y = pdfread.getNumPages()

str = ""
for i in range(1,y) :
    str += pdfread.getPage(i).extractText()

with open(txtpath, 'w', encoding = "utf-8") as f:
     f.write(str)

print(str)
