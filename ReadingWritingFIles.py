import os
import shelve
import shutil

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
baconFile = open('bacon.txt', 'w')
baconFile.write("Bacon is not a vegtable but that is ok")
baconFile.close()
baconFile = open('bacon.txt', 'a')
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

#with copy if you just put folder it keeps the same name
shutil.copy('bacon.txt', 'morebacon.txt')

#copytree will copy the whole folder you would use the follow
#shutil.copytree('c:\\basedir','c:\\destinationdir')
#move will wait for it... move a file
#shutil.move('c:\\spam.txt','c:\\delicious')
#there is no rename so you would use move
#shutil.move('c:\\spam.txt','c:\\morespam.txt')

#Deleting files
#os.unlink('bacon.txt')
#delete a directory
#os.rmdir('c:\\delicious')
#folder needs to completly for this to work
#to remove an entire folder wihfiles
#shutil.rmtree('c:\\delicious')

#is a good idea when using unlink, rmdir and rmtree that you do a dry run
#        for filename in os.listdir():
#           if filename.endswith('.rtx'):
#               #os.unlink(filename)
#               print(filename)
#       Here we do a dry run a kick output to print so that we can see what we would delete before do it


# there is a module called send2trash that can be used, need to install with pip
# has a method called send2trash that put in bin
# send2trash.send2trash('somefile.txt')


for folderName, subfolders, filenames in os.walk('c:\\TEMP'):
    print('The folder is ' + folderName)
    print('The subfolders in ' + folderName + ' are : ' + str(subfolders))
    print('The filesnames in ' + folderName + ' are ' + str(filenames))
    print()



