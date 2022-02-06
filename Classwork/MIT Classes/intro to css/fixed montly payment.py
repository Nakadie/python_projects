balance = 3754
annualInterestRate = 0.18 
#b = balance
monthlyInterestRate  = annualInterestRate/12

payment = 0
bal = balance


months=11
while bal >= 0: 
    bal = balance
    while months>=0:

        bal  -= payment
        bal  += bal *monthlyInterestRate
        
        months -= 1
    payment  += 10
    months = 11
    

print("lowest Payment:", (payment-10))