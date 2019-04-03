# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 04:38:41 2019

@author: Anjani K Shiwakoti
"""

def general_poly (L):
    
    """ 
    L, a list of numbers or coefficients (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 
    """
    def translate_string(any_string, super_or_sub):
        if super_or_sub == 'SUB':
            to_string = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
        elif super_or_sub == 'SUP':
            to_string = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
    
        return any_string.translate(to_string)
    
    def func_in_poly(x):
    
        num_count = len(L)
        
        poly_list = []
        poly_expr = []
        
        for i in range(num_count):
            coefficient = L[i]
            exponent = (num_count-1)-i
            poly_list.append( coefficient * (x**exponent))
            
            poly_expr.append(str(coefficient) + "x" + translate_string(str(exponent),'SUP'))
            
        return (poly_expr, poly_list, sum(poly_list))
    
    return func_in_poly(len(L))

# get all values from above functions
polynomial_expression, polynomials, polynomial_sum = (general_poly ([1,5,9,2,6,7,3,8,4]))
print()
print ("Polynomial Sum = ", end ='') 
for element in polynomial_expression:
    print (element, end='')
    if element != polynomial_expression[-1]:
        print (' + ', end='')
print()
print ("Polynomial Sum = ", end ='')   
for element in polynomials:
    print (element, end='')
    if element != polynomials[-1]:
        print (' + ', end='')
print()
print ("Polynomial Sum = ", polynomial_sum)
 
"""
OUTPUT: 
Polynomial Sum = 1x⁸ + 5x⁷ + 9x⁶ + 2x⁵ + 6x⁴ + 7x³ + 3x² + 8x¹ + 4x⁰
Polynomial Sum = 43046721 + 23914845 + 4782969 + 118098 + 39366 + 5103 + 243 + 72 + 4
Polynomial Sum =  71907421
"""
