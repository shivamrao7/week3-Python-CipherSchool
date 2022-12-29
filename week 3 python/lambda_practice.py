def is_even(a):
    return a%2==0
    # if a%2==0:
    #     return True
    # return False
print(is_even(5))
iseven2 = lambda a: a%2==0
print(iseven2)

def last_char(s):
    return s[-1]
last_char = lambda s: s[-1]
print(last_char("kuanl"))


# lambda with if , else

# def func(s):
#     if len(s) > 5:
#         return True
#     return False

func = lambda s: True if len(s) > 5 else False
print(func('abcdefg'))

print(func('abc'))


# same func in short
# def func(s):
#     return len(s)>5
func = lambda s:  len(s) > 5 

