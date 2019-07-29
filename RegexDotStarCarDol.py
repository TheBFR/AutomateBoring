import re

beginsWithRegex = re.compile(r'^Hello')
mo = beginsWithRegex.search('Hello there!')
print(mo.group())

mo = beginsWithRegex.search('He said Hello there!')
if mo != None:
    print(mo.group())
else:
    print("I found nothing that matches")

beginsWithRegex = re.compile(r'world!$')
mo = beginsWithRegex.search('Hello world!')
print(mo.group())

beginsWithRegex = re.compile(r'world!$')
mo = beginsWithRegex.search('Hello world are you ready!')
if mo != None:
    print(mo.group())
else:
    print("I found nothing that matches")

allDigitsRegex = re.compile(r'^\d+$')
mo = allDigitsRegex.search('798347502938457')
print(mo.group())

allDigitsRegex = re.compile(r'^\d+$')
mo = allDigitsRegex.search('79834750x2938457')
if mo != None:
    print(mo.group())
else:
    print("I found nothing that matches")

# . stands for any character but a new line
atRegex = re.compile(r'.at')
mo = atRegex.findall('The cat in the hat sat on the flat mat')
print(mo)

# . stands for any character but a new line, no we add {}
atRegex = re.compile(r'.{1,2}at')
mo = atRegex.findall('The cat in the hat sat on the flat mat')
print(mo)

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.findall('First Name: Troy Last Name: Downing')
print(mo)

serve = '<To serve humans> for dinner.>'
nongreedy = re.compile(r'<(.*?)>')
mo = nongreedy.findall(serve)
print (mo)

greedy = re.compile(r'<(.*)>')
mo = greedy.findall(serve)
print (mo)

prime = 'Serve the public trust.\nProtect the innocent.\nUphold the law.'
print(prime)

dotStart = re.compile(r'.*')
mo = dotStart.search(prime)
print(mo.group())

dotStart = re.compile(r'.*', re.DOTALL)
mo = dotStart.search(prime)
print(mo.group())

vowelRegex = re.compile(r'[aeiou]')
mo = vowelRegex.findall('Al, why does your programming book talk about RoboCop so much?')
print(mo)

vowelRegex = re.compile(r'[aeiou]', re.IGNORECASE) #re.I is the same
mo = vowelRegex.findall('Al, why does your programming book talk about RoboCop so much?')
print(mo)
