# *operator
# *args

# def total(a,b):
#     return a+b

# def all_total(*args):
#     print(args)
#     print(type())


# all_total(1,2,3,4,5,65)

# *ARGS in sabhi ka tuple bnaye ga
#  change in tuple 

def total(a,b):
    return a+b

def all_total(*args):
    total = 0
    for num in args:
        total += num
    return total
print(all_total(1,2,3,4,65))