def department_summary(employees):
    print("Employee Details:")
    dic={}
    count=0
    for employee in employees:
        department = employee["department"]
        salary = employee["salary"]
        name = employee["name"]

        if department not in dic:
            dic[department] = {"count": 0,
                            "total_salary": salary,
                            "max_salary": salary,
                            "max_salary_employee": name}

        else:
            dic[department]["count"] += 1
            dic[department]["total_salary"] += salary
            
            if salary > dic[department]["max_salary"]:
                dic[department]["max_salary"] = salary
                dic[department]["max_salary_employee"] = name

    results = {}
    for department in dic:
        count =dic[department]["count"]
        avg_salary = dic[department]["total_salary"]/count
        highest_employee_name = dic[department]["max_salary_employee"]
        
        results[department] = (count, avg_salary, highest_employee_name)
        
    return results

employees=[
        {"name": "Abhay","department": "engineering","salary":85000},
        {"name": "Khushal","department": "engineering","salary": 87000},
        {"name": "Dhruvil","department": "sales","salary": 68000},
        {"name": "Vyom","department": "sales","salary": 64000}
        ]

print(department_summary(employees))
    
