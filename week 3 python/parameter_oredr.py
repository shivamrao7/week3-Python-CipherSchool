# default paramateres = num
# def func(num,**kwargs)

# def func(name = 'unknown' , age =24):
#     print(name)
def func(name,*args, last_name = 'unknown', **kwargs):
    print(name)
    print(args)
    print(last_name)
    print(kwargs)

func('kunal', 1,2,3,a = 1, b =1)