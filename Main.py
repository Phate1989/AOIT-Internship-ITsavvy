import csv

Requirements = ["Exchange Online (Plan 2) Corporate", "Power BI Pro Corporate"]
OpenReqs = Requirements

Bundle = []
BundleMatches = []
SA_Prices = []
SA_Total = 0
SubsToRemove = []
BundlePrice = 0
SubsRemoved = []

# reading in SKU List
with open('AOIT_Internship_Excel.csv', 'r') as file:
    SKUList = csv.DictReader(file)
    line_count = 0
    SKUs = []
    # creating SKU List
    for sku in SKUList:
        SKUs.append(sku)
    #    print(row)

# Reading in bundle Info
with open('Bundle_Spreadsheet.csv', 'r') as file:
    reader = csv.DictReader(file)
    line_count = 0
    List = []
    # creating Bundle Info List
    for row in reader:
        List.append(row)
        # print(row)


#Find Bundle Matches for Requirements
for Req in Requirements:
    for row in List:
        for k, BundleSKU in row.items():
            if Req == BundleSKU:
                BundleMatches.append({"Sub": Req, "Bundle": k})


print(BundleMatches)




#Find Most Common Bundle
track = {}

for FoundMatch in BundleMatches:
    for key, value in FoundMatch.items():
        if key == "Bundle":
            if value not in track:
                track[value] = 0
            else:
                track[value] += 1

MostCommonBundle = (max(track, key=track.get))


#find subs in most common Bundle
for lines in List:
    SubsToRemove.append(lines[MostCommonBundle])
print(SubsToRemove)


#Remove From Open Requirements

for SubToRemove in SubsToRemove:
    for OpenReq in Requirements:
        if OpenReq == SubToRemove:
            SubsRemoved.append(OpenReq)
            OpenReqs.remove(SubToRemove)
print(OpenReqs)





# Get Stand Alone Price
for Req in SubsRemoved:
    for SkuMatch in SKUs:
        if Req == SkuMatch['Description (Product) (Product)']:
            SA_Prices.append({"Sub": Req, "Price": SkuMatch['Manufacturers List Price (Product) (Product)']})

for subs in SA_Prices:
    SA_Total += float(subs['Price'])

#Gets matching BUndle and Price
for SkuMatch in SKUs:
    if MostCommonBundle == SkuMatch['Description (Product) (Product)']:
        BundlePrice = float(SkuMatch['Manufacturers List Price (Product) (Product)'])

print("Standard Total: " + str(SA_Total))
print("Bundle Total: " + str(BundlePrice))
#print(SA_Total)

        # Find SubProducts
for lines in List:
    Bundle.append(lines['Office 365 E3 Corporate'])

# based on input of Exchange online plan 2 and Apps for Enterprise, we need to find
# 1. The price of those items
# 2. All bundles that include those items
# 3. The price of those bundles
