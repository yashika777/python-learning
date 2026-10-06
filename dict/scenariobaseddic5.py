# Create a nested dictionary for employee details:
# pythonemployees = {
#     "E001": {"name": "Rajesh", "salary": 50000, "dept": "IT"},
#     "E002": {"name": "Priya", "salary": 60000, "dept": "HR"}
# }
# Write a program to:
# Print Rajesh's salary
# Add a new employee E003
# Find all employees in IT department
# Give 10% raise to all employees
pythonemployees = {
    "E001": {"name": "Rajesh", "salary": 50000, "dept": "IT"},
    "E002": {"name": "Priya", "salary": 60000, "dept": "HR"}
}
print(pythonemployees["E001"]['salary'])
pythonemployees['E003']={
    'name':'Palak','salary':65000,'dept':'IT'
}
for key,value in pythonemployees.items():
        if value['dept']=='IT':
                print(value['name'])
        value['salary']*=1.1
print(pythonemployees)


