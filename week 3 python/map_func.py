numbers = [1,2,3,4]
def square(a):
    return a**2
squareslambda  = list(map(lambda a:a**2, numbers))

squares = list(map(square, numbers))
print(squares)
# is map object ko list or tuple me convert jkar sakte ha``

# list comp
squares_new = [i**2 for i in numbers]
print(squares_new)

names = ['abc', 'abcd', 'abcde']
length = map(len, names)
for i in len:
    print(i)

for j in length:
    print(j)