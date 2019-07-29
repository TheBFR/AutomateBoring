#answer = input('Would you like to play again?')
answer = 'no'
print(answer)


if answer.islower == True:
    print('The user typed in all lower case', answer)
elif answer.lower() == 'yes':
    print('The user typed in a mixed case ', answer)
elif answer.lower() == 'no':
    print('The user typed in a mixed case ', answer)
else:
    print('Its a yes or no question, no game for you')

print('Hello'.upper().isupper())

# isalpha - letters only
# - isalnum - letter and numbers only
# - isdecimal - numbers only
# - isspace - whitespace only
# istitle - titlecase only, I.E. begings will upper case followed only by lowercase, all the words in string

print('Hello World'[5].isspace())

print('Hello World'.startswith('Hell'))
print('Hello World'.startswith('ell'))
print('Hello World'.endswith('rld'))
print('Hello World'.endswith('Wor'))

allTheAts = ','.join(['cats','bats','rats'])
print (allTheAts)

print('My name is Troy'.split())
print('My name is Troy'.split('m'))
print('Hello'.ljust(10))
print('Hello'.ljust(10,'*'))
print('Hello'.rjust(10))
print('Hello'.rjust(10, '*'))
print('Hello'.center(20))
print('Hello'.center(20, '*'))
spam = 'Hello'.rjust(10)
print (spam)
print(spam.strip())
spam = '     x     '
print(spam)
print(spam.lstrip())
print(spam.rstrip())
print(spam.strip())
spam = 'SpamSpamBaconSpamEggsSpamSpam'.strip('ampS')
print(spam)
spam = 'Hello there!'
print (spam.replace('e', 'XYZ'))

import pyperclip
pyperclip.copy('Hello!!!!!')
print(pyperclip.paste())