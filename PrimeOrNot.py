a=int(input("Enter a number:"))
if a>1:
    for i in range(2,a-1):
        if a%i==0:
            print(a,"is not prime") 
            break
    else:       
        print(a,"is prime")
else:
    print(a,"is not prime")
