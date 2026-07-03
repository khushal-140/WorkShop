# H2) E-Commerce Price Filter
# Products are sorted by price. Find the first product whose price is greater than or equal to ₹50,000. 

price=[1000,2000,3000,4000,5000,6000,7000,8000,9000,10000]
key=5000
low=0
high=len(price)-1
answer=0


while low<=high:
    mid=(low+high)//2

    if key<price[mid]:
        answer=mid
        high=mid-1
    else:
        low=mid+1
        
print("First Product Price Found at index:",answer)
print("Product Price:",price[answer])
