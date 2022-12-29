# # d = {'name' : 'unknown', 'age' : 'unknown'}
# d = dict.fromkeys(['name','age','height'], 'unknown')
# d = dict.fromkeys(range(1,11), 'unknown')
# d = dict.formkeys(['name', 'age'], ['unknown', 'unknown'])
# # d = dict.formkeys(('name', 'age','height'))
# # from keys method is used to create dictionary

# get method(useful)
d = {'name' : 'kunal', 'age' : 'unknown'}
# print(d['name']) 

# print(d.get('name'))

# if 'name' in d:
#     print('present')
# else:
#     print('not present')

# if d.get('name'):
#     print('present')
# else:
#     print('not present')

# # if none---> False, elsetRUE-->

# d1  = d.copy()
# d1 = d
# print(d1.popitem())
# print(d)

# # d1 AND d are same dict

# print(d1 is d)

print(d["name"])
print(d.get("name"))
print(d.popitem())