# no=[40,30,10,2,3]
# for i in range(len(no)):
#     for j in range(len(no)-i-1):
#         if no[j]>no[j+1]:
#             temp=no[j]
#             no[j]=no[j+1]
#             no[j+1]=temp
# print(no)

# no=[40,30,10,2,3]
# for i in range(len(no)):
#     for j in range(i+1,len(no)):
#         if no[i]>no[j]:
#             temp=no[i]
#             no[i]=no[j]
#             no[j]=temp
# print(no)
            
    
# name=["Ravi","Ramesh","Suresh","Mahesh"]
# key="Ramesh"
# found=0
# for i in range(len(name)):
#     if name[i]==key:
#         print(key,"Found at index:",i)
#         found=1
#         break
# if found==0:
#     print(key,"Not found")
    


word=["Aple","Banana","Cat","Dose","Elephant"]
key="Aple"
low=0
high=len(word)-1
while low<=high:
    mid=(low+high)//2
    if word[mid]==key:
        print(key,"Found at index:",mid)
        break
    elif key<word[mid]:
        high=mid-1
    else:
        low=mid+1   
        
