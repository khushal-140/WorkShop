regions={}
f=open("Sales Summary Report Generator.csv","r")
for line in f:
    info=line.split(",")
    date=info[0]
    region=info[1]
    product=info[2]
    unit=int(info[3])
    selling=int(info[4].strip())
    
    if region not in regions:
        regions[region]={
            "total_revenue": 0,
            "total_units": 0,
            "products": {}
        }

    regions[region]["total_revenue"] +=selling
    regions[region]["total_units"] += unit
    
    if product in regions[region]["products"]:
        regions[region]["products"][product] += unit
    else:
        regions[region]["products"][product] = unit    
        
    
    
    
       
f.close()
for region in regions:
    
    products = regions[region]["products"]

    best_product = ""
    highest_units = -1

    for product in products:

        if (products[product] > highest_units or
            (products[product] == highest_units and product < best_product)):

            highest_units = products[product]
            best_product = product

    regions[region]["best_product"] = best_product

print(regions)
