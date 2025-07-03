# This program calculates the total monthly expenses for rent and electricity, and divides 
# it among a specified number of persons.

# Input: Rent amount, electricity bill amount, charges per unit of electricity, and number 
# of persons sharing the expenses.
rent=float(input("Enter the rent amount: "))
electricity_bill=float(input("Enter the electricity bill amount: "))
charges_per_unit=float(input("Enter the charges per unit of electricity: "))
person=int(input("Enter the number of persons sharing the expenses: "))

# Calculation of total expenses
# and per person expense
# Total bill for electricity is calculated by multiplying the electricity bill with charges per unit
# Total expense is the sum of rent and total electricity bill
# Per person expense is calculated by dividing the total expense by the number of persons
# Total bill for electricity


total_bill=electricity_bill * charges_per_unit
total_expense=rent + total_bill

# Calculating per person expense


per_person_expense=total_expense / person


# Output: Total bill for the month


print("Total bill for the month: ", per_person_expense)