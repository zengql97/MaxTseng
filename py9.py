def make_incrementor(n):
    return lambda x: x-n
f = make_incrementor(4)#n
print(f(1))#x
