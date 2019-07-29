myList = [1,2,3,4,5]

for i in range(len(myList)):
    print (myList[i])

print ("1 is in list myList in index slot",myList.index(1))
# if you do this and there are repeats then it will just return index of first occurrence

print(myList)

myList.append(6)

print(myList)

myList.insert(2,15)

print(myList)

myList.remove(15)
# if you do this and there are repeats then it will just remove first occurrence

print(myList)

del myList[0]

print(myList)

myOrderedList = [10,6,8,12,14,45,1,19]
print (myOrderedList)
myOrderedList.sort()
print (myOrderedList)
myNameList = ['Troy', 'Tobias', 'Ruby', 'Kathy']
print (myNameList)
myNameList.sort()
print (myNameList)
myNameList.sort(reverse=True)
print (myNameList)
# If the list has both string and numbers(integers or floats) it cant sort it
myMixList = ['A','z','b','x','T','F','Z','a','b','n','M']
print (myMixList)
myMixList.sort()
print (myMixList)
# Also case sorting is based on ASCII so capital letters come first
# for true sort you can pass
myMixList.sort(key=str.lower)
print (myMixList)