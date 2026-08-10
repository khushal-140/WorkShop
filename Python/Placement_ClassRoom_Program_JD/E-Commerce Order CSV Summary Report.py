f=open("E-Commerce Orders.csv","r")
total=0
dic={}
high=0
customer_total = {}
highest_customer=""
for line in f:
    
    data=line.strip().split(",")
    if data[3].strip()=="":
        continue
    
    order_id=data[0]
    customer_name=data[1]
    category=data[2]
    amount=float(data[3])
    
    if data[4].strip()=="Completed":  
        total+=amount
    if category in dic:
        dic[category]+=1
    else:
        dic[category]=1
        
        
        
        
        
        
    if data[4].strip()=="Completed":
        if customer_name in customer_total:
            customer_total[customer_name] +=amount
        else:
            customer_total[customer_name]=amount

for customer in customer_total:
    if customer_total[customer] > high:
        high = customer_total[customer]
        highest_customer = customer            

print("Total Amount of Completed Orders:",total)
print("category order",dic)
print(highest_customer,"amount",high)
