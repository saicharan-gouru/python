def fib_term(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        return fib_term(n-1)+fib_term(n-2)

n=int(input("Enter n value : "))
print("The required term is",fib_term(n))
