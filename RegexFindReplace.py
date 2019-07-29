import re

namesRegex = re.compile(r'Agent \w+')
mo = namesRegex.findall('Agent Alice gave the secret documents to Agent Bob.')
print(mo)
mo = namesRegex.sub('REDACTED', 'Agent Alice gave the secret documents to Agent Bob.')
print(mo)

#now we will replace with part of original
namesRegex = re.compile(r'Agent (\w)\w*')
mo = namesRegex.findall('Agent Alice gave the secret documents to Agent Bob.')
print(mo)
mo = namesRegex.sub(r'Agent \1****', 'Agent Alice gave the secret documents to Agent Bob.')
print(mo)

#verbose mode allows the addition of comments to help document complicated regex expressions
commentRegex = re.compile(r'''
(\d\d\d-) |      # area code (without parens, with dash)
(\(\d\d\d\) )    # -or- area coe with parens no dash
\d\d\d           #second 3 digits
-                #second dash
\d\d\d\d')       #last 4 digits
\sx\d{2,4}    # extension like x1234''',re.VERBOSE)

#can use multiuple re.compile flags with |
commentRegex = re.compile(r'''
(\d\d\d-) |      # area code (without parens, with dash)
(\(\d\d\d\) )    # -or- area coe with parens no dash
\d\d\d           #second 3 digits
-                #second dash
\d\d\d\d')       #last 4 digits
\sx\d{2,4}    # extension like x1234''',re.IGNORECASE | re.DOTALL | re.VERBOSE)