# l  = [1,2,3]
# if l:
#     print("not empty")
# else:
#     print("empty")

def to_power(num, *args):
    if args:
        return [i**num for i in args]
    else:
        return "you didint pass any args"
nums = [1,2,4,5]
print(to_power(9,*[2,5]))