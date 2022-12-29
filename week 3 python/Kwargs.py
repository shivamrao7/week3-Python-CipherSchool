# KWARGS(KEYWORD ARGUMENT)
# **kwargs (double star operator)

# kwargs me kitne keyword dal sakte ha je usko dictionary me gather kardega

# KWARGS AS A PARAMETER
def func(**kwargs):
    print(kwargs)
    for k,v in kwargs.items():
        print(f"{k},{v}")

func(first_name = "kunal" , last_elemnet = "sarpal")

def func(name,**kwargs):
    print(kwargs)
    for k,v in kwargs.items():
        print(f"{k},{v}")

# func('mmohit',first_name = "kunal" , last_elemnet = "sarpal")

# dictionary unpacking
d = {'name':'kunal', 'age': 24}
func(**d)