"""

from itertools import tee
import os 

all_file=os.listdir(r'C:\Users\Kishor Kore\Desktop\motor sample')
print(all_file)

c=0
from pdfminer.high_level import extract_text
text10 = extract_text(r"C:\Users\Kishor Kore\Desktop\motor sample\{}".format("Motor Truck Cargo Schedule Of Coverages -1.pdf"))

for i in all_file:
    from pdfminer.high_level import extract_text

    text11 = extract_text(r"C:\Users\Kishor Kore\Desktop\motor sample\{}".format(i))
    if text10==text11:
        print("-------------",i)


"""





