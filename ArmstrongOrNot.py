'''
An armstrong number is any number of n digits which is equal to the sum of nth power of digits in the number. 
Generally in most programming cases we consider numbers from 000 to 999 that is 3 digit numbers. Thus, we also define 
armstrong number is any number of 3 digits which is equal to sum of cubes of digits in number.
'''
Num=int(input('Enter A Number:'))
Temp=Num
Order=len(str(Num))
Sum=0
while(Num>0):
    Rem=Num%10
    Sum=Sum+Rem**Order
    Num=Num//10
if Sum==Temp:
    print(Temp,'is armstrong')
else:
    print(Temp,'is not armstrong')
    
