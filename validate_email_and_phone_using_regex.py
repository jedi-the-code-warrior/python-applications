
import re
import string

# reviews = ["I don't know about you but I like Apple better than Google. Apple has better employee satisfaction than Google.",
#            "Microsoft is also a great place to work but I sometimes don't like their policies. I'd prefer NetFlix if I could choose between FAANGs.",
#            "Facebook is also one of my dream places to work. I admire Facebook's employee compensation plans but lately I am hesitant to apply at Facebook because of thier political involvement regarding consumer privacy.",
#            "Microsoft and Amazon are among my top 5 places to work, but if I were given a choice, I would choose one from Google, Apple, LinkedIn, and NetFlix.",
#            "Apple is definitely the best place to work for me because I personally like and use their products and Apple has always stood out as a cool company."]

# for quote in reviews:
#     word_list = re.sub(r'[^\w=]', ' ',quote)

#     print(word_list)

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
