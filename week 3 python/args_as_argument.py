# function ko call karte ha to argument
# define karte ha to parameter

def multiply_nums(*args):
    multiply = 0
    # print(num)
    # print(args)
    for i in args:
        multiply *= i
    return multiply

nums = [4,5,1]
print(multiply_nums(*nums))
# star likhne se completly unpack ho jaye ga
