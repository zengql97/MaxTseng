#learning git
for n in range(2,10):
    for x in range (2,n):
        if n % x ==0:
            print (n,'equals',x,'*',n//x)
            break
    else :#this else is for the for X part
            print(n,'is a prime number')
