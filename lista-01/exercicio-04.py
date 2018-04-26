salary = float(input('Salary:'))
percent = float(input('Increase %:'))  / 100
new_salary = salary + (salary * percent)

print('New salary', new_salary)