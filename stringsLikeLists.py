#Strings and Lists are similar in many ways, some of the same methods work
stringList = list('Hello')
print(stringList)
name = 'RatFink'
print (name[0])

print (name[1:3])

# But there is a difference, strings are Immutable, where as lists are Mutable
# as they can have items added and removed

# when a variable is assigned by another variable its value dues not changes when the original variable is changes
cat = 4
print (cat)
dog = cat
print (dog)
cat = 3
print (cat)
print (dog)

#but with a list the varibale is just a pointer or refeence to the list so when it the list is updated
#all variables pointing to the list will return the same value
ogList = [1,2,3,4,5]
print (ogList)
dosList = ogList
print (dosList)
dosList.append(6)
print (ogList)
print (dosList)

# can use copy module via import copy and then use copy.deepcopy that creates a brand new list with a separate reference 