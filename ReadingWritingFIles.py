import os
import shelve

myFile = open('.\\workingwithfiles.txt')
print(myFile.read())
myFile.close()
#you can only read a file once, have to close and reopen to read again so put in variable instead

myFile = open('.\\workingwithfiles.txt')
myFileRead = myFile.read()
myFile.close()
print(myFileRead)

#readlines returs a list of string
myFile = open('.\\workingwithfiles.txt')
myLines = myFile.readlines()
myFile.close()
print(myLines)

#open with w will write to the file, if not exsist it will create, if exsist it will overwrite
helloFile = open('.\\helloworld.txt', 'w')
helloFile.write("OMG I am wirting to a file")
helloFile.write("OMG I am wirting to a file")
helloFile.write("OMG I am wirting to a file")
helloFile.close()

print(os.getcwd())
baconFile = open('.bacon.txt', 'w')
baconFile.write("Bacon is not a vegtable but that is ok")
baconFile.close()
baconFile = open('.bacon.txt', 'a')
baconFile.write("\nWe need more bacon flavored vegtables")

#shelve files
shelfFile = shelve.open('mydata')
shelfFile['cats'] = ['Garfield','Vincent','Scratchy','Tom','Kitty']
shelfFile.close()

shelfFile = shelve.open('mydata')
myCats = shelfFile['cats']
shelfFile.close()
print(myCats)

shelfFile = shelve.open('mydata')
print(list(shelfFile.keys()))
print(list(shelfFile.values()))

