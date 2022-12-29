# s = {k**2 for k in  range(1,11)}
# print(s)
# # set or dict ka koi order nih hota

# names = ['harshit', 'mohit', 'rohit']
# fist= {names[0] for name in names}
# print(fist)

a = {"math":20,"bio":30,"english":40}
b = {"math":40,"bio":60,"english":30}
c = [a,b]
d = input("enter nnumber")
for i in c:
    f = []
    if d == a:
        for k,v in a.items():
            print(v)
            f.append(v)
        print(f)
        q = f.pop(0)
        w = f.pop()
        e = f.pop()
        print((q+w+e)/3)
    elif d==b:
        print("else is printing")
        for k,v in b.items():
            print(v)
            f.append(v)
        
        q = f.pop(0)
        w = f.pop()
        e = f.pop()
        print((q+w+e)/3)

    else:
        print()


        