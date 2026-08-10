try:
    f=open("Unique_Visitor_Log.txt","r")
    unique=[]
    total_requests=0;
    most_page="";
    most_count=0;
    dic={}

    for line in f:
        info=line.strip().split(" - ");
        unique.append(info[0])
        total_requests +=1
        page=info[2]
        #total_requests.append(info[0])
        if page in dic:
            dic[page] +=1
        else:
            dic[page] =1
        #Most   Visited Page
        if dic[page] >= most_count:
            most_count=dic[page]
            most_page=page
        
        
        
        
        
    f.close()
    print("Total Unique Visitors:",len(set(unique)))
    print("Total Requests:",total_requests)
    print("Most Visited Page:",most_page,"count:",most_count)



except FileNotFoundError:
    print("Unique_Visitor_Log.txt not found.")