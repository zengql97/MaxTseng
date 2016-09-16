#this is a program used to search prime numbers
x = int(input('give me a range, I will help you to find prime numbers from 2 to that number'))

def prime(n):
 if n == 2 : print ('2')
 elif n > 2 :
    for i in range(2,n+1):
     for j in range(2,int(i**0.5+1)):
        if i % j == 0 : break
     else: print (i, 'is a prime number')

prime(x)
