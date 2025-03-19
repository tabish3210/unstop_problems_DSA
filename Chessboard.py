import sys
s=input()
a = {'a':1,'b':2,'c':3, "d":4, 'e':5, "f":6, "g":7,"h":8}
n=int(s[1])%8
if (a[s[0]]+n)%2==0:
  print("Black")
else:
  print('White')
                  
