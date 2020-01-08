# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 04:38:41 2019

@author: Anjani K Shiwakoti

This is my own method for generating polynomial expressions and their sums.

"""

def general_poly (L,x=2):
    
    """ 
    x = 2, variable is initialized with base 2 but can be overridden by any integer
    L, a list of numbers or coefficients (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the
    expression: n0 * x^k + n1 * x^(k-1) + ... nk * x^0 
    values: val(k)+ val(k-1) + ... +val(0)
    sum: sum of all values
    
    """
    def translate_string(any_string, super_or_sub):
        if super_or_sub == 'SUB':
            to_string = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
        elif super_or_sub == 'SUP':
            to_string = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
    
        return any_string.translate(to_string)
    
    def func_in_poly(num_count):
    
        k = num_count
        
        poly_list = []
        poly_expr = []
        
        for i in range(k):
            coefficient = L[i]
            exponent = (k-1)-i
            poly_list.append( coefficient * (x**exponent))
            
            poly_expr.append(str(coefficient) + "x" + translate_string(str(exponent),'SUP'))
            
        return (poly_expr, poly_list, sum(poly_list))
    
    return func_in_poly(len(L))

# grab all values from above functions and display
polynomial_expression, polynomials, polynomial_sum = general_poly ([1,5,9,2,6,7,3,8,4])
print()
print ("Polynomial Expression = ", end ='') 
for element in polynomial_expression:
    print (element, end='')
    if element != polynomial_expression[-1]:
        print (' + ', end='')
print()
print ("Polynomial Interim = ", end ='')   
for element in polynomials:
    print (element, end='')
    if element != polynomials[-1]:
        print (' + ', end='')
print()
print ("Polynomial Sum =",polynomial_sum)

#--------------------------------------------------------------------------------------------------------------------------------------
"""
OUTPUT: 
Polynomial Expression = 1x⁸ + 5x⁷ + 9x⁶ + 2x⁵ + 6x⁴ + 7x³ + 3x² + 8x¹ + 4x⁰
Polynomial Interim = 256 + 640 + 576 + 64 + 96 + 56 + 12 + 16 + 4
Polynomial Sum = 1720
"""
