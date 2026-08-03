employees=[
    {
    "name": "Amit",
    "department": "engineering",
    "salary": 75000
    },
    {
          "name": "Sneha",
          "department": "engineering",
          "salary": 82000
      },
      {
          "name": "Rahul",
          "department": "sales",
          "salary": 54000
      },
      {
          "name": "Priya",
          "department": "sales",
          "salary": 61000
      }
      ]
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
                           "highest_salary": salary,
                           "highest_salary_employee": name}

    else:
        dic[department]["count"] += 1
        dic[department]["total_salary"] += salary
        
        if salary > dic[department]["highest_salary"]:
            dic[department]["highest_salary"] = salary
            dic[department]["highest_salary_employee"] = name

# results = {}
# for department in dic:
#     count =dic[department]["count"]
#     total_salary = dic[department]["total_salary"]/count
#     highest_salary = dic[department]["highest_salary"]
    
#     results[department] = (count, total_salary, highest_salary)
    
# print(results)