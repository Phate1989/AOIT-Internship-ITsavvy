import csv


with open('Bundle_Spreadsheet.csv', 'r') as file:
    reader = csv.DictReader(file)
    line_count = 0
    List = []
    for row in reader:
        List.append(row)
    #    print(row)


# print()
    # print(list)
    # print()
    # print(list[0][0])

for lines in List:
    print(lines['Office 365 E3'])


