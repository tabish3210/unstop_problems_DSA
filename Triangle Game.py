import sys

def pascal(n):
    row=[1]
    for k in range(1, n+1):
        element=row[k-1]*(n-k+1) // k
        row.append(element)
    return row

if __name__ =="__main__":
    n=int(sys.stdin.read().strip())
    result=pascal(n)
    sys.stdout.write(" ".join(map(str, result))+ "\n")
