#Question Write a Python program to print the Fibonacci series.
# no=int(input("Enter Number:"))
# a=0
# b=1
# for i in range(no):
#     print(a,end=" ")
#     c=a+b
#     a=b
#     b=c




# Write a Python program to calculate the ticket price based on age.
# no= int(input("Enter Number: "))
# if no<=5:
#     print("Ticket price 0")
# elif no>5 and no<=18:
#     print("Ticket price 5")
# elif no>18 and no<=60:
#     print("Ticket price 10")
# else:
#     print("Ticket price 12")
    
    
    
    
    
    
#Triagle Pattern 
# no= int(input("Enter Number: "))
# for i in range(1,no+1):
#     for j in range(i):
#         print("*",end="")
#     print()
    
#Triangle NNumber Pattern
# no= int(input("Enter Number: "))
# for i in range(1,no+1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()

#Center Triangle Pattern
# no= int(input("Enter Number: "))
# for i in range(1,no+1):
#     print(" "*(no-i),end="")
#     print("*"*i)

#Q Great! Printing alphabet patterns is almost the same as printing numbers or stars. The only difference is that we use letters instead of * or numbers.

for i in range(65, 70):
    print(chr(i))
    
for i in range(65, 70):
    for j in range(65, i+1):
        print(chr(j), end="")
    print()