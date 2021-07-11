'''
Lapindrome is defined as a string which when split in the middle, gives two halves having the same characters and same frequency of each character. If there are odd number of characters in the string, we ignore the middle character and check for lapindrome. For example gaga is a lapindrome, since the two halves ga and ga have the same characters with same frequency. Also, abccab, rotor and xyzxy are a few examples of lapindromes. Note that abbaab is NOT a lapindrome. The two halves contain the same characters but their frequencies do not match.
'''

n = input()
l = len(n)
if l % 2 == 0:
    b, c = n[:l//2], n[l//2:]
else:
    b, c = n[:l//2], n[l//2+1:]
if sorted(b) == sorted(c):
    print("YES")
else:
    print("NO")