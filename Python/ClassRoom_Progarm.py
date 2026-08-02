list=[{
    "name": "John",
    "department": "engineering",
    "salary": 50000
    },
      {
          "name": "Alice",
          "department": "marketing",
          "salary": 60000
      },
      {
          "name": "Bob",
          "department": "sales",
          "salary": 55000
      }]
print("Employee Details:")
counteng = 0
countmar = 0
countsal = 0
for employee in list:
    print("Name:", employee["name"])
    print("Department:", employee["department"])
    print("Salary:", employee["salary"])
    if employee["department"] == "engineering":
        counteng += 1
    if employee["department"] == "marketing":
        countmar += 1
    if employee["department"] == "sales":
        countsal += 1
print("Number of employees in the engineering department:", counteng)
print("Number of employees in the marketing department:", countmar)
print("Number of employees in the sales department:", countsal)