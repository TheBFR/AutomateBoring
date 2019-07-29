import re

#This fucntion is without Regex
def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'

print('415-555-4242 is a phone number:')
print(isPhoneNumber('415-555-4242'))
print('Moshi moshi is a phone number:')
print(isPhoneNumber('Moshi moshi'))

for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
print('Done')

#you will usually pass raw strings to re.compile(), which creates the regex object
#the r is for raw so the \ is not seen as an escape character
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
#mo variable is shore for matched object, search creates a match object
mo = phoneNumRegex.search(message)
#group() is the match object to get matched string
print('This is from mo ' + mo.group())
#to find all the occurances use the findall re menthod
print(phoneNumRegex.findall(message))




#This is the fucntion using Regex


