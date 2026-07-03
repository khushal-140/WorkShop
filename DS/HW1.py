# H1) The Spam Detector
# Incoming emails are checked against a blacklist. The blacklist has no order.

blacklist=["abc@gmail.com","xyz@gmail.com","pqr@gmail.com","admin@gmail.com"]
email="admin@gmail.com"
found=0
for i in range(len(blacklist)):
    if blacklist[i]==email:
        print(email,"is blacklisted email")
        found=1
        break
if found==0:
    print(email,"is not blacklisted")
    