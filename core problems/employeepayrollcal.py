def employee_payroll_calculator():
    name = input("Enter employee name: ")
    base_salary_input = input("Enter base salary: ")
    base_salary = float(base_salary_input)
    bonus_input = input("Enter bonus percentage: ")
    bonus_percentage = float(bonus_input)
    bonus_amount = (base_salary * bonus_percentage) / 100
    total_salary = base_salary + bonus_amount
    print("Employee Name:", name)
    print("Base Salary:", base_salary)
    print("Bonus Percentage:", bonus_percentage)
    print("Bonus Amount:", bonus_amount)
    print("Total Salary:", total_salary)

employee_payroll_calculator()