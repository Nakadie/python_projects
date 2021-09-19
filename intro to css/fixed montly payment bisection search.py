#starting variables.
balance = 999999
annualInterestRate = 0.18
monthlyInterestRate  = annualInterestRate/12

def findendbal(balance, payment):
    bal = balance
    for months in range(1,13):
    
        bal  -= payment
        bal  += bal *monthlyInterestRate
       
    return bal

upper = (balance*(1 + monthlyInterestRate)**12)/12.0
lower = balance / 12
payment = (lower + upper)/2 

while abs(findendbal(balance, payment)) >= .03:
    
    payment = (lower + upper)/2 
    if findendbal(balance, payment) >= .03:
    
        lower = payment
    elif findendbal(balance, payment) < -.03:
        upper = payment
    payment = (lower + upper)/2     
print(round(payment,2))
   
    
   
