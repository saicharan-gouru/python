"""
To find the lcm or hcf of a given array or list of elements we use 'reduce' function
-It first apply the given function on first 2 elements of array or list
-Next it apply the given function on (result of first two elements) and third element
-The process continues until the array or list of elements are computed

"""


from functools import reduce

def HCF(a,b):
    if b==0:
        return a
    return HCF(b,a%b)
  
def LCM(a,b):
    return a*b//HCF(a,b)

a=[]
n=int(input("Enter Number Of Elements:"))
for i in range(n):
    a.append(int(input("Enter "+str(i+1)+" Element:")))
ch=input("\n 1.HCF \n 2.LCM \n Enter Your Choice:")
if(ch=='1'):
    res=reduce(HCF,a)
    print("HCF Of Given Array Of Elements : ",res)
if(ch=='2'):
    res=reduce(LCM,a)
    print("LCM Of Given Array Of Elements : ",res)
if(ch != '1' and ch != '2'):
    print("Enter valid choice i.e. Either 1 or 2")
