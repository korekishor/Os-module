# import PyPDF2
# file = open('C:\\Users\\Kishor Kore\\Downloads\\Kishor-Genre\\OneDrive_2_7-28-2022\\14\\Dean Transportation 2021 Auto FAC Certificate.pdf','r')
# readpdf = PyPDF2.PdfFileReader(file)
# totalpages = readpdf.numPages
# print(totalpages)
# file.close()


# from frontend import *
# import fitz
# # Open the PDF file using the open() function and store it in a variable.
# gvn_pdffile = fitz.open(r'C:\\Users\\Kishor Kore\\Downloads\\Kishor-Genre\\OneDrive_2_7-28-2022\\14\\Dean Transportation 2021 Auto FAC Certificate.pdf')
# # Apply pageCount on the above pdf file to get the count of total number of 
# # pages in a given PDF file and print the result.
# print("The total number of pages in the given PDF file: ")
# print(gvn_pdffile.pageCount)
# """
# from pdfminer.high_level import extract_text
# import shutil
# import os
# all_file=os.listdir(r'C:\Users\Kishor Kore\Desktop\Kishor-Genre\OneDrive_2_7-28-2022')

# text10 = extract_text(r"C:\Users\Kishor Kore\Desktop\Kishor-Genre\OneDrive_2_7-28-2022", page_numbers = range(0,4))



# from pdfminer.pdfparser import PDFParser
# from pdfminer.pdfdocument import PDFDocument
# from pdfminer.pdfpage import PDFPage
# from pdfminer.pdfinterp import resolve1

# file = open('C:\\Users\\Kishor Kore\\Downloads\\Kishor-Genre\\OneDrive_2_7-28-2022\\14\\Dean Transportation 2021 Auto FAC Certificate.pdf', 'rb')
# parser = PDFParser(file)
# document = PDFDocument(parser)

# # This will give you the count of pages
# print(resolve1(document.catalog['Pages'])['Count'])


from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
import os 
import shutil
from pdfminer.pdfinterp import resolve1

count1=0

all_file=os.listdir(r'C:\Users\Kishor Kore\Desktop\Kishor-Genre\OneDrive_2_7-28-2022')
print(all_file)

page_count=0

for i in all_file:

    file = open(r"C:\\Users\\Kishor Kore\\Desktop\\Kishor-Genre\\OneDrive_2_7-28-2022\\{}".format(i),'rb')
    parser = PDFParser(file)
    document = PDFDocument(parser)
    page_count=resolve1(document.catalog['Pages'])['Count']
    list.append(page_count)
    try:
        if page_count==3:
            hitun_ghe = r"C:\Users\Kishor Kore\Desktop\Kishor-Genre\OneDrive_2_7-28-2022\{}".format(i)
            hite_tak = r"C:\Users\Kishor Kore\Desktop\Kishor-Genre\folder_3\{}".format(i)
            shutil.move(hitun_ghe, hitun_ghe)
    except:
        pass






# for i in range(len(list)):
#     if list[i]==2:
#         src_path = r"C:\Users\Kishor Kore\Desktop\Kishor-Genre\OneDrive_2_7-28-2022\{}".format(all_file[i])
#         dst_path = r"C:\Users\Kishor Kore\Desktop\Kishor-Genre\w2\{}".format(i)
#     elif list[i]==3:
#         src_path = r"C:\Users\Kishor Kore\Desktop\Kishor-Genre\OneDrive_2_7-28-2022\{}".format(all_file[i])
#         dst_path = r"C:\Users\Kishor Kore\Desktop\Kishor-Genre\w3\{}".format(i)