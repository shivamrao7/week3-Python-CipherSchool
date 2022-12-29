# set data type
# Un ordered collection of unique item
s = {1,2,3,2}

# we cant do any indexing
l = [1,2,3,4,45,5,6,6,6,6,7,7,8,9,9]
# remove duplicate
s2 = list(set(l))
print(s2)
s3  = {1,1.0,2.3,'string'}
# add eelemt in set
s.add(4)
s.add(5)

# s.remove(4)
# s.discard(5)
print(s)
s.clear
print(s)

s1 = s.copy()
print(s1)

# order koi matter nhi karta same in dict