import re
#? says that the proceeding group can occur 0 or 1 time in order for a match to occur
batRegex = re.compile(r'Bat(wo)?man')
mo = batRegex.search('The Adventures of Batman')
print(mo.group())
mo = batRegex.search('The Adventures of Batwoman')
print(mo.group())
mo = batRegex.search('The Adventures of Batwowowoman')
if mo == None:
    print("No matches")

phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneRegex.search('My phone number is 415-555-1234. Call me tomorrow')
print(mo.group())
mo = phoneRegex.search('My phone number is 555-1234. Call me tomorrow')
if mo == None:
    print("No matches")
phoneRegex = re.compile(r'(\d\d\d)?\d\d\d-\d\d\d\d')
mo = phoneRegex.search('My phone number is 555-1234. Call me tomorrow')
print(mo.group())

#* says that  proceeding group can occur 0 or more time in order for a match to occur
batRegex = re.compile(r'Bat(wo)*man')
mo = batRegex.search('The Adventures of Batman')
print(mo.group())
mo = batRegex.search('The Adventures of Batwoman')
print(mo.group())
mo = batRegex.search('The Adventures of Batwowowoman')
print(mo.group())

#+ means that proceeding has to match once
batRegex = re.compile(r'Bat(wo)+man')
mo = batRegex.search('The Adventures of Batman')
if mo == None:
    print("No matches")
mo = batRegex.search('The Adventures of Batwoman')
print(mo.group())
mo = batRegex.search('The Adventures of Batwowowoman')
print(mo.group())

#here we escape the above regex times to match them in a regex
regex = re.compile(r'\+\*\?')
mo = regex.search("I learned about +*? regex syntax")
print(mo.group())

#{x} x is match at least
haRegex = re.compile(r'(Ha){3}')
mo = haRegex.search('He said "HaHaHaHa"')
print(mo.group())

#combining matching itesm
phoneRegex = re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(,)?){3}')
mo = phoneRegex.search('My numbers are 415-555-1234,555-4242,212-555-0000')
print(mo.group())

#{xy} x at least, y at most. nothing before comma is 0, nothing after would be unlimited
haRegex = re.compile(r'(Ha){3,5}')
mo = haRegex.search('He said "HaHaHaHa"')
print(mo.group())
mo = haRegex.search('He said "HaHaHaHaHaHaHa"')
print(mo.group())

#by default python regex does greedy matches, so takes longest possible string
digitRegex = re.compile(r'(\d){3,5}')
mo = digitRegex.search('1234567890')
print(mo.group())

#to do non greeedy (shorted possible)  after {x,y} add a ?
digitRegex = re.compile(r'(\d){3,5}?')
mo = digitRegex.search('1234567890')
print(mo.group())
