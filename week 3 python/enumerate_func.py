# we use this function with for loop to track position of our item

# without enumeratae func
names = ['abc', 'abcdef', 'kunal']
pos = 0
for name in names:
    print(f"{pos}---->{name}")
    pos+=1

# with enumerate function

for pos, name in enumerate(names):
    print(f"{pos}---->{name}")



def find_pos(l,target):
    for pos, name in enumerate(l):
        if name == target:
            return pos
        return -1
