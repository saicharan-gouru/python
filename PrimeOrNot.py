'''
A prime number is a positive integer having exactly two factors. If p is a prime, then it’s only factors are necessarily 1 and p itself. Any number which does not follow 
this is termed as composite numbers, which means that they can be factored into other positive integers.

First Ten Prime Numbers

The first ten primes are 2, 3, 5, 7, 11, 13, 17, 19, 23, 29.
'''
a=int(input("Enter a number:"))
flag=0
if a>1:
    for i in range(2,a):
        if a%i==0:
            flag=1
    if flag==1:
        print(a,"Is Not Prime")
    else:
        print(a,"Is Prime")
else:
    print(a,"Is Not Prime")
    
