import re
phoneNumber=re.compile(r'\d\d\d-\d\d')
mo=phoneNumber.search('my phone number is 333-22')
print('Phone number found: '+mo.group())