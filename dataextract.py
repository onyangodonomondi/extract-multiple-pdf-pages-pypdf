from PyPDF2 import PdfFileReader, PdfFileWriter

file_path = 'Automate.pdf'
pdf = PdfFileReader(file_path)


# Lecture Note.txt is the file for the data that is going to be extracted.  You can cgage it to your liking.
with open('Lecture Note.txt', 'w') as f:
    for page_num in range(pdf.numPages):
        # print('Page: {0}'.format(page_num))
        pageObj = pdf.getPage(page_num)

        try:
            txt = pageObj.extractText()
            print(''.center(100, '-'))
        except:
            pass
        else:
            f.write('Page {0}\n'.format(page_num+1))
            f.write(''.center(100, '-'))
            f.write(txt)
    f.close()
