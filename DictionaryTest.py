myCat = {'size':'fat','name':'bob','age':'5'}
yourCat = {'size':'skinny','age':'12','name':'boris'}

for k in myCat.keys():
    print(k)

for v in myCat.values():
    print(v)

for i in myCat.items():
    print(i)

print (myCat)

myCatAge = myCat.get('age',0)
print(myCatAge)

myCatColor = myCat.get('color','Not Specified')
print(myCatColor)

if 'color' not in myCatColor:
    myCat['color']='black'
myCatColor = myCat.get('color','Not Specified')
print(myCatColor)

print(yourCat)
yourCat.setdefault('color','orange')
print(yourCat)