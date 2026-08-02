list=[
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
countdep=0
countdep1=0
avg_salary=0
for employee in list:
    if employee["department"] == "engineering":
        countdep += 1
        
        avg_salary += employee["salary"]
        avg_salary = avg_salary / countdep
        dic[employee["department"]] =(countdep, avg_salary,employee["name"])
    if employee["department"] == "marketing":
        countdep += 1
        avg_salary += employee["salary"]
        avg_salary = avg_salary / countdep
        dic[employee["department"]] =(countdep, avg_salary,employee["name"])
    if employee["department"] == "sales":
        countdep1 += 1
        avg_salary += employee["salary"]
        avg_salary = avg_salary / countdep1
        dic[employee["department"]] =(countdep1, avg_salary,employee["name"])
print(dic)        