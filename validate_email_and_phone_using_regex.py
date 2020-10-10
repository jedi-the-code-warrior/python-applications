
import re
import string

### some useful string manipulation functions

alpha = string.ascii_letters
print(alpha)
lower = string.ascii_lowercase
print(lower)
digits = string.digits
print(digits)
punc = string.punctuation
print(punc)

phone_cleaned=''
phone_cleaned_list=[]

### validate phone numbers using regular expression
phone_list = ['415/859-8447', '888*859*8447', '(800) 859-8447', '415.555.9999','[909] 123-4567']
for phone in phone_list:
    #phone_cleaned = re.sub(r'[\s\[\]/*().-]', '',phone)
    #phone_cleaned = re.sub(r'[^0-9]', '',phone)
    #phone_cleaned = re.sub(r'[\D]', '',phone)
    #phone_cleaned = re.sub(r'[^\d]', '',phone)
    phone_cleaned = re.sub(rf"[\b{punc}\b ]", "", phone)
    phone_cleaned_list.append(phone_cleaned)

print(phone_cleaned_list)

### validate email address using regular expression

emails = ['someagency@state.gov', 'someorg@nonprofit.org', 'someone@company.com', 'first.last@gmail.com', 'first_last@hotmail.com']

result = {}
for email in emails:
	valid = False
	pattern = re.search()

	result[email] = valid 
print(result)
