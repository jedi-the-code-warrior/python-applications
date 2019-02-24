# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 1:53:02 2018

@author: Anjani K Shiwakoti

    Synopsis: Given the current credit card balance and annual interest rate, 
    calculate the fixed minimum monthly payment which if paid monthly pays off the 
    entire credit card balance in one year (12-month term)

    Monthly interest rate = (Annual interest rate) / 12.0
    Monthly payment lower bound = Balance / 12
    Monthly payment upper bound = (Balance x (1 + Monthly interest rate)^12) / 12.0

    Input:balance (int/float), annualInterestRate (float)
    Operation: Perform a bisection search on lower and upper bound
    Output: Print minimum fixed monthly payment (as part of a string)
"""

# initialize variables
term = 12 
monthCount = 0
monthlyUnpaidBalance = 0.0
newMonthlyBalance = 0.0
monthlyPayment = 0.0

# assign given value of balance to a new variable so that the balance remains unchanged
newMonthlyBalance = balance

# convert given annualInterestRate to monthly rate
monthlyInterestRate = (annualInterestRate)/12.0

# we know that the absolute monthly minimum cannot be less than balance divided by number of months
lowerBound = balance/term

# we know that the absolute maximum cannot be more than balance + interest divided by number of months
upperBound = (balance * (1 + monthlyInterestRate)**term)/term  

# very small marker for testing, can be lower
epsilon = 0.05
      
while (abs(newMonthlyBalance) > epsilon):

    # reset the value of newMonthlyBalance to original balance until less than 0
    newMonthlyBalance = balance
    monthlyPayment = (lowerBound + upperBound)/2
       
    # calculate monthlyUnpaidBalance, plug them in formula to obtain new monthly balance   
    for monthCount in range(term) :   
        monthlyUnpaidBalance = (newMonthlyBalance) - (monthlyPayment)
    
        newMonthlyBalance = ((monthlyUnpaidBalance) \
                          + (monthlyInterestRate \
                          * monthlyUnpaidBalance))
                          
    # approximate monthlyPayment by bisection search
    if (newMonthlyBalance > epsilon):
        lowerBound = monthlyPayment
        
    elif (newMonthlyBalance < -epsilon):
        upperBound = monthlyPayment
        
    else:
        # format the result to 2 decimal places and print it as string     
        print ("Lowest Payment: " + str(round(monthlyPayment, 2)))
        break
        
# end of while loop