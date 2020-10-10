# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 13:48:16 2020

@author: Anjani K Shiwakoti

A palindromic number reads the same both ways. For example, 1234321 is a palindrome. 
The largest palindrome made from the product of two two-digit numbers is 9009 = 91 × 99. 
Find the largest palindrome made from the product of two three-digit numbers.


"""



def largest_two_3digit_product_palindrome():
    """ 
    Computes largest palindrome made from the product of two 3-digit numbers
    
    output: dictionary with two 3-digit palindromes as key (tuple) and a whole number as the highest product value (an integer)
    """
    
    def is_palindrome(xnum):
        """
        Returns True if number is a palindrome, False otherwise
        """
        
        ### cast numbers into string
        str_num=str(xnum)
        
        for i in range(len(str_num)//2):
            if str_num[i] != str_num[-i-1]:
                ### if digits/characters don't match, return false
                return False  
            
            else: continue  ### keep looping through the next pair of characters
        
        ### only if left side matches with the right side we get here
        ### this means all lef-right characters match...so return true
        return True

    largest_palindrome_dict = {'Max Value':None}
    current_largest = 0

    for n1 in range(999, 99, -1):   ### it's not necessary to iterate below 500 but did it anyway
   
        for n2 in range(999, 99, -1):  ### it's not necessary to iterate below 500 but did it anyway
            
            product = n1*n2

            if product < current_largest: 
                continue

            if is_palindrome(product):

                current_largest = max(current_largest, product)
            
                largest_palindrome_dict['Max Value'] = str(n1)+' X '+str(n2)+' = '+ str(current_largest) ### nested dict

     
    return largest_palindrome_dict 
    

largest_palindrome_dict = largest_two_3digit_product_palindrome()
print(largest_palindrome_dict)

# this outputs only the key (not the associated value)
#largest_palindrome = max(palindromes_dict, key=palindromes_dict.get)
#print(largest_palindrome)

### this outputs both the key-value pairs in tuple format, by maximum key 
### to get the key-value pairs by maximum value then do key=lambda x: x[1]
#largest_palindrome = max(palindromes_dict.items(), key=lambda x: x[1])
#print(largest_palindrome)

    

