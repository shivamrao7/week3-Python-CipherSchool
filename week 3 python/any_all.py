def my_sum(*args):
    # total = 0
    if all([type(arg) == int or type(arg)==float for arg in args]):
        total = 0
        for num in args:
            total += num
        return total
    else:
        return "wrng input"

print(my_sum(1,2,3,4,5,'kunal',['kunal']))