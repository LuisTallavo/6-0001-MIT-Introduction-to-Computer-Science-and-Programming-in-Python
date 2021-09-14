import math

portion_down_payment = 0.25
current_savings = 0.0
annual_rate = 0.04
months = 0

annual_salary = float(input("Please enter the starting annual salary: "))
portion_saved = float(input ("Please enter the portion that is saved every month from your starting salary: "))
total_cost = float(input("Please enter the total cost of your dream home: "))
semi_annual_raise = float(input("Please enter the semi-annual salary raise: "))

down_payment = total_cost * portion_down_payment

while current_savings < down_payment:
    months += 1
    if months % 6 == 0:
        annual_salary = annual_salary * (1 + semi_annual_raise)
    current_savings += current_savings * annual_rate/12
    current_savings += (portion_saved * annual_salary) / 12

print(math.ceil(months))
