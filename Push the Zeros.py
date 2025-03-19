n=int(input())
lst=list(map(int,input().split()))
non_zeros=[i for i in lst if i!=0]
zeroes=[i for i in lst if i==0]
result=non_zeros+zeroes
print(" ".join(map(str,result)))
