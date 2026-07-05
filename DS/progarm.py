# #Linear Search Algorithm
# number=[10,20,30,40,50]
# found=0
# no=int(input("Enter Number: "))
# for i in range(len(number)):
#     if number[i]==no:
#         print(no,"Number Found at index:",i)
#         found=1
#         break
# if found==0:
#     print(no,"Number Not Found")        



# no=[10,20,70,80,90,100]
# low=0
# high=len(no)-1
# key=90
# while low<=high:
#     mid=(low+high)//2
#     if no[mid]==key:
#         print(key,"Number Found at index:",mid)
#         break
#     elif key<no[mid]:
#         high=mid-1
#     else:
#         low=mid+1



# number=[4,7,1,2,30]
# for i in range(len(number)):
#     for j in range(i+1,len(number)):
#         if number[i]>number[j]:
#             temp=number[i]
#             number[i]=number[j]
#             number[j]=temp
# print(number)

# for i in range(len(number)):
#     for j in range(len(number)-i-1):
#         print(number[j])

def binary_search(li,low,high,key):
    if low>high:
        return -1
    mid=(low+high)//2
    if li[mid]==key:
        return mid
    elif key<li[mid]:
        return binary_search(li,low,mid-1,key)
    else:
        return binary_search(li,mid+1,high,key)
    
list1=[10,20,30,40,50]
key=10
result=binary_search(list1,0,len(list1)-1,key)
if result != -1:
    print(key,"Element found at index", result)
else:
    print("Element not found")