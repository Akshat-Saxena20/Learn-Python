n=int(input("Enter the number of employees: "))
employees={}
for i in range(n):
    name=input('Enter the name of employee: ')
    salary=input('Enter the salary of an employee: ')
    employees[name]=salary

while True:
    name=input('Enter the employee name: ')
    salary=employees.get(name,-1)
    if salary == -1:
        print('Employee does not exist')
    else:
        print('The Salary of employee is: ',salary)  

    choice=input('Do you want to know an other employee salary [Yes|No]: ')
    if choice == 'No':
        break          