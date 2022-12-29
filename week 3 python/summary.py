a = dict(name="kunal", b = 'sarpal')
print(a)

for key,value in a.items():
    print(key,value)

print(a.get('b'))
a[1] = "123"