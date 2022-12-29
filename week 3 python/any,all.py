numbers1 = [2,4,6,8,10]
numbers2 = [1,2,3,4,5,6]

evens1 = []
for num in numbers1:
    if num%2==0:
        evens1.append(num%2==0)

print(all([True, False, True, True,True]))
print(any([True, False, True, True,True]))

print(all([num%2 == 0 for num in numbers1]))
print(any([num%2 == 0 for num in numbers1]))