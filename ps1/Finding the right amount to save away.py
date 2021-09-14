import math

def savings_36_months(savings_rate, annual_salary, down_payment, semi_annual_raise):
    months = 36
    current_savings = 0.0

    for i in range(months):
        if (i + 1) % 6 == 0:
            annual_salary = annual_salary * (1 + semi_annual_raise)
        current_savings += current_savings * annual_rate/12
        current_savings += (savings_rate * annual_salary) / 12
    return current_savings
    

def binary_search (array, target, annual_salary, semi_annual_raise):
    if len(array) - 1 >= 1:
        midpoint = len(array) // 2
        
        savings_rate = array[midpoint] / 1000000
        
        current_savings = savings_36_months(savings_rate, annual_salary, target, semi_annual_raise)

        if current_savings > target - 10 and current_savings < target + 10:
            return savings_rate
        elif current_savings > target + 10:
            return binary_search(array[:midpoint], target, annual_salary,semi_annual_raise)
        elif current_savings < target - 10:
            return binary_search(array[midpoint:], target, annual_salary,semi_annual_raise)
    else:
        return None

portion_down_payment = 0.25
current_savings = 0.0
annual_rate = 0.04
semi_annual_raise = 0.07
total_cost = 1000000.0
months = 36.0

annual_salary = float(input("Please enter the starting annual salary: "))
down_payment = portion_down_payment * total_cost

target_list = range(0, 10000000)

result = binary_search(target_list, down_payment, annual_salary, semi_annual_raise)

if result == None:
    print("It is not possible to save for the down payment in 3 years")
else:
    print(result)
