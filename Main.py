import csv

Bundle = []


with open('AOIT_Internship_Excel.csv', 'r') as file:
    SKUList = csv.DictReader(file)
    line_count = 0
    SKUs = []

    for sku in SKUList:
        SKUs.append(sku)
    #    print(row)


with open('Bundle_Spreadsheet.csv', 'r') as file:
    reader = csv.DictReader(file)
    line_count = 0
    List = []

    for row in reader:
        List.append(row)
        #print(row)

for lines in List:
    Bundle.append(lines['Office 365 E3 Corporate'])

for subSKU in Bundle:
   

    # for sub in Bundle:
    # if sub in
