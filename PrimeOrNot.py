a=int(input("Enter a number:"))

for i in range(2,a-1):
    if a%i==0:
        print(a,"is not prime")
else:        
    print(a,"is prime")
