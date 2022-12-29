a = ['abc','tuv','xyz']
b = [i[::-1] for i in a]
print(b)

def revverse(l):
    new = []
    for i in l:
        new.append(i[::-1])
    return new
print(revverse(a))
