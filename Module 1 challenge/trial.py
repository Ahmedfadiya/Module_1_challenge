import csv
from pathlib import Path


loan_costs = [500, 600, 200, 1000, 450]

# How many loans are in the list?
# @TODO: Use the `len` function to calculate the total number of loans in the list.
# Print the number of loans from the list
number_of_loans = len(loan_costs)
print(f"There are {number_of_loans} number of loans")

total_loan = sum(loan_costs)
print(f"The total value of loans are{total_loan} ")
average_loan = sum(loan_costs) / len(loan_costs)
print(f"The average loan amount is {average_loan}.")

loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

future_value = loan.get("future_value")
remaining_months = loan.get("remaining_months")
print(f"the future value is $ {future_value}")
print(f"The remaining months are {remaining_months}")

discount_rate = .2
present_value = future_value / (1+ discount_rate/12) ** remaining_months
print(f"The present value is $ {present_value: .2f}")

# If Present Value represents what the loan is really worth, does it make sense to buy the loan at its cost?
# @TODO: Write a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.
#    If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
#    Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.
# YOUR CODE HERE!
loan_cost = loan.get("loan_price")
print(f"The loan cost is: $ {loan_cost}")
if present_value >= loan_cost:
    print(f"The loan is worth at least the cost to buy it.")
elif present_value <= loan_cost:
    print(f"The loan is too expensive and not worth the price.")

# Given the following loan data, you will need to calculate the present value for the loan
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# @TODO: Define a new function that will be used to calculate present value.
#    This function should include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
#    The function should return the `present_value` for the loan.

annual_discount_rate = 0.20
def calculate_present_value(future_value, annual_discount_rate, remaining_months):
    present_value = (future_value / (1+ (annual_discount_rate/12)) ** remaining_months)
    return present_value

present_value = calculate_present_value(new_loan["future_value"], annual_discount_rate, new_loan["remaining_months"])
print(f"The current price is $ {present_value: .2f}")    

loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]
inexpensive_loans = []
for loan in loans:
    if loan["loan_price"]<=500:
        inexpensive_loans.append(loan)
for loan in inexpensive_loans:
    print(loan)

csvpath = Path('inexpensive_loans.csv')
with open(csvpath, "w", newline="") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow("header")
    for row in loans:
        csvwriter.writerow(loan.values())

    
