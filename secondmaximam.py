#  5
#  6,5,8,3,9
#  output

# n=int(input("enter the no of digit : "))
# l=[]
# for i in range(n):
#     s=int(input())
#     l.append(s)
# s=[]
# for i in range(n):
#     m=max(l)
#     s.append(m)
#     l.remove(m)

# print("max number in list are : ",s[1])

# from PyPDF2 import PdfFileWriter, PdfFileReader
# inputpdf = PdfFileReader(open("input.pdf", "rb"))
# for i in range(inputpdf.numPages):
#     j = i+1    
#     output = PdfFileWriter()
#     output.addPage(inputpdf.getPage(i))
# with open("page%s.pdf" % j, "wb") as outputStream:
#     output.write(outputStream)



# n1,n2=0,1
# for i in range(5):
#     n3=n1+n2
#     print(n3)
#     n1,n2=n2,n3




# def rec(n1,n2):
#     n3=n1+n2
#     print(n3)
#     if n3>15:
#         print()
#     else:
#         n1,n2=n2,n3
#         rec(n1,n2)

# rec(0,1)


