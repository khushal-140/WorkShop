# H3) IRCTC Waitlist Merger
# Two already sorted lists. Merge them.

# li1=[7,5,3,1,2,4,6]
# li2=[10,11,9,8,12,13,14]
# l3=li1+li2
# for i in range(len(l3)):
#     for j in range(i+1,len(l3)):
#         if l3[i]> l3[j]:
#             temp=l3[i]
#             l3[i]=l3[j]
#             l3[j]=temp
# print(l3)
    
    
li1=[1,5,8]
li2=[2,4,9]

merged=[]
i=0
j=0
while i<len(li1) and j<len(li2):
    if li1[i]<li2[j]:
        merged.append(li1[i])
        i+=1
    else:
        merged.append(li2[j])
        j+=1
        
while i<len(li1):
    merged.append(li1[i])
    i+=1
while j<len(li2):
    merged.append(li2[j])
    j+=1
    
    
print(merged)
