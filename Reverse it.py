# Enter your code here. Read input from STDIN. Print output to STDOUT

x,y=input().split()
if y not in x:
  print(x)
else:
  r=""
  for i in range(len(x)-1,-1,-1):
    if x[i]==y:
      r=x[i:][::-1]
      idx=i 
      break
  res=x[:idx]+r
  print(res)
