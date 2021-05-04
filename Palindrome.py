'''
A palindrome is a word, number, phrase, or other sequence of characters which reads the same backward as forward, such as madam or 
racecar.
'''
A=input('Enter a word, number, phrase, or other sequence of characters:')
print('Given input:',A)
S=A[::-1]
if S==A:
    print('Given Input Is Palindrome :)')
else:
    print('Given Input Is Not Palindrome :( , Try Another One')
