# Dictionary Methods

info = {'name':'Vaibhav', 'age':19, 'eligible':True}
print(info)
#Update()   
info.update({'age':22})
info.update({'DOB':2001})
print(info)
ing = {'name':'Vaibhav', 'age':19, 'eligible':True}
print(ing)
#clear()
ing.clear()
print(ing)
#pop()
info.pop('DOB')
print(info)
#popitem()
info.popitem()
print(info)
#del
del info['age']
print(info)
del ing
