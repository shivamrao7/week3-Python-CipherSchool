numbers  = [1,2,3,4]
# , tuples , string ----iterables
squares = list(map(lambda a:a**2, numbers))

# for i in numbers:
#     print(i)
# for i in squares:
#     print(i)

# map object pe for loop chali

# step call iter function
# iter(number)  --->

# for loop aise kam karte ha
number_iter = iter(numbers)
print(next(number_iter))
print(next(number_iter))
print(next(number_iter))
print(next(number_iter))
print(next(number_iter))

# print(iter(numbers)) ---- ek object ha

print(next(squares))
print(next(squares))
print(next(squares))





print(squares)