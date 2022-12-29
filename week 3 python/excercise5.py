def func(l, **kwargs):
    if kwargs.get('reverse_str') == True:
        return [name[::-1].title() for name in l]
    else:
        return 

# kwargs args normal default

def func2(name, *args, last_name = 'unkwon', **kwargs):
    print(name)
    print(args)
    print(last_name)
    print(
        kwargs)
func2('harshit', 1,2,3.4,78,8, a = 1, b = 2, c = 4)


    
