#! python3

import re, pyperclip

#Create a regext for phone numbers
phoneRegex = re.compile(r'''
#415-555-1234, 555-0000, (413) 555-0000, 555-0000 ext 12345, ext. 12345, x12345
(
((\d\d\d) | (\(\d\d\d\)))?    #are code (optional)
(\s|-)    #first sperattor
\d\d\d    #first 3 digits
-    #seperator
\d\d\d\d   #last 4 digits
(((ext(\.)?\s)|x)      #extension word part (optional)
(\d{2,5}))?     #extension number part(optional)
)
''',re.VERBOSE)


#Create a regex for eamil addresses
emailRegex = re.compile(r'''
#some.+_thing@something.com

[a-zA-Z0-9_.+]+    # name part
@    # @ sign
[a-zA-Z0-9_.+]+    #domain name part
''',re.VERBOSE)

# Get text off the clipboard or from file
text = pyperclip.paste()

#Extract the email/phoen from this list
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

print(allPhoneNumbers)
print(extractedEmail)

#Copy the extracted email/phone to clipboard or write out to new file
results  = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)