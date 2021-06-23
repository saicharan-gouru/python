def romanToInt(self, s: str) -> int:
     roman={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
     num=0
        
     for i in s[::-1]:
         res=roman[i]
         if 4*res < num:
             num-=res
         else:
             num+=res
        
     return num
       
number=int(input())
print(romanToInt(number))
