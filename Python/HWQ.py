''''
print("1.Decimal to Binary")
print("2.Decimal to Octal")
print("3.Decimal to Hexadecimal")
print("4.Binary to Decimal")
print("5.Octal to Decimal")
print("6.Hexadecimal to Decimal")
print("0.Exit")
choice = int(input("Enter your choice: "))
while choice != 0:
    if choice == 1:
        no = int(input("Enter Number: "))
        print(bin(no))
    elif choice == 2:
        no = int(input("Enter Number: "))
        print(oct(no))
    elif choice == 3:
        no = int(input("Enter Number: "))
        print(hex(no))
    elif choice == 4:
        no = input("Enter Binary Number: ")
        print("Decimal =", int(no, 2))
    elif choice == 5:
        no = input("Enter Octal Number: ")
        print("Decimal =", int(no, 8))
    elif choice == 6:
        no = input("Enter Hexadecimal Number: ")
        print("Decimal =", int(no, 16))
    else:
        print("Invalid Choice")
'''



'''
    0-50 = 3.25
    51-100 = 4.80
    101-200 = 6.30
    201-300 = 7.40
    above 300 = 8.50
'''

# units=int(input("Enter Units: "))
# if units<=50:
#     bill=units*3.25
# elif units<=100:
#     bill=(50*3.25)+((units-50)*4.80)
# elif units<=200:
#     bill=(50*3.25)+(50*4.80)+((units-100)*6.30)
# elif units<=300:
#     bill=(50*3.25)+(50*4.80)+(100*6.30)+((units-200)*7.40)
# else:
#     bill=(50*3.25)+(50*4.80)+(100*6.30)+(100*7.40)+((units-300)*8.50)
# print("Electricity Bill =", bill)


f=open("marks","r")
for line in f:
    data=line.strip().split()
    name=data[0]
    fail=[]
    english=int(data[1])
    science=int(data[2])
    math=int(data[3])
    if 40>english:
        fail.append("e")
    if 40>science:
        s=name
        fail.append("s")
    if 40>math:
        m=name
        fail.append("m")
    
    if len(fail)==0:
        total=data[1]+data[2]+data[3]
        print(name,total)

    else:
        print(name,",".join(fail))

f.close()