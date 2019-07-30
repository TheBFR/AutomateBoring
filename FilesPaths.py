import os
myPath = os.path.join('folder1','folder2','folder3','folder4')
print(myPath)
currentWD = os.getcwd()
print(currentWD)
os.chdir('c:\\')
newWD = os.getcwd()
print(newWD)
os.chdir(currentWD)
whereAMI = os.getcwd()
print(whereAMI)

myFile = os.path.abspath('FilesPaths.py')
print(myFile)

noAbs = os.path.isabs('.\\FilePath.py')
yesAbs = os.path.isabs('c:\\')
print(noAbs,'',yesAbs)

print(os.path.relpath('c:\\folder1\\folder2\\spam.png', 'c:\\folder1'))
print(os.path.dirname('c:\\folder1\\folder2\\spam.png'))
print(os.path.basename('c:\\folder1\\folder2\\spam.png'))
print(os.path.basename('c:\\folder1\\folder2'))

print(os.path.exists('c:\\'))
print(os.path.exists('c:\\troy'))
print(os.path.isfile('c:\\'))
print(os.path.isdir('c:\\'))

print(os.path.getsize('c:\\windows\\system32\\calc.exe'))
print(os.listdir('c:\\'))

totalSize = 0
for filename in os.listdir('c:\\'):
    if not os.path.isfile(os.path.join('c:\\', filename)):
        continue
    totalSize = totalSize + os.path.getsize(os.path.join('c:\\', filename))

print(totalSize)

#making dirs os.makedirs('c:\\delicious\\walnut\\waffles')
#this would create all 3 directoies if they did not exsist

