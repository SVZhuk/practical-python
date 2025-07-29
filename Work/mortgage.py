# mortgage.py
#
# Exercise 1.7

# Dave has decided to take out a 30-year fixed rate mortgage of $500,000 with
# Guido’s Mortgage, Stock Investment, and Bitcoin trading corporation. The
# interest rate is 5% and the monthly payment is $2684.11.

principal = 500000.0
interest_rate = 0.05
monthly_payment = 2684.11
total_paid = 0.0

while principal > 0:
    principal = principal * (1 + interest_rate / 12) - monthly_payment
    total_paid = total_paid + monthly_payment

print(f"Total amount paid over the life of the mortgage: ${total_paid:.2f}")

# Exercise 1.8 Extra Payments
# Suppose Dave pays an extra $1000/month for the first 12 months of the mortgage?
# Modify the program to incorporate this extra payment and have it print the total
# amount paid along with the number of months required. When you run the new program,
# it should report a total payment of 929,965.62 over 342 months.

principal = 500000.0
total_paid = 0.0
interest_rate = 0.05

extra_payment = 1000.0
months = 0

while principal > 0:
    if months < 12:
        principal = principal * (1 + interest_rate / 12) - (
            monthly_payment + extra_payment
        )
    else:
        principal = principal * (1 + interest_rate / 12) - monthly_payment
    total_paid += monthly_payment + (extra_payment if months < 12 else 0)
    months += 1

print(f"Total amount paid with extra payments: ${total_paid:.2f}")
print(f"Number of months to pay off the mortgage: {months}")

# Exercise 1.9 Extra Payments Calculator
# Modify the program so that extra payment information can be more generally 
# handled. Make it so that the user can set these variables:
# extra_payment_start_month = 61
# extra_payment_end_month = 108
# extra_payment = 1000