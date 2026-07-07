def crash_report(filepath):
    try:
        f=open(filepath+".txt","r")
        count=0
        transention=0
        corr=0
        for line in f:
            try:
                data=line.strip().split("|")
                status=data[3].strip()
                amount=float(data[2].strip())
                
                if status == "FAILED":
                    count +=1
                    transention +=amount
                    
                    print(status)
            except (IndexError,ValueError):
                corr=+1
        f.close()
        return ("count:",count,"amount:",transention,"corr:",corr)
    except(FileNotFoundError):
        print("File Not Found")    

print(crash_report("QQ"))
        