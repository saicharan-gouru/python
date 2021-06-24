'''
We can say the given string is a 'Pangram' when the string consists all the alphabets from a to z, if anyone letter is missing we can say that it is not a pangram
'''
def pangram(s):
    alphabet="abcdefghijklmnopqrstuvwxyz"
    for i in alphabet:
        if i not in s:
            return False
    return True

string = input()
if(pangram(string)):
    print(string+" is a pangram")
else:
    print("sorry")
