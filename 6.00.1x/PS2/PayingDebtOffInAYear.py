__author__ = 'ThanhNam'

balance = 3329
annualInterestRate = 0.2

monthlyPayment = 0
monthlyInterestRate = annualInterestRate /12
newBalance = balance
month = 0

while newBalance > 0:
    monthlyPayment += 10
    newBalance = balance

    for month in range(1,13):
        newBalance -= monthlyPayment
        newBalance += monthlyInterestRate * newBalance
        month += 1
print 'Lowest Payment: ', monthlyPayment