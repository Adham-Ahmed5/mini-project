inpooo=int(input())

f=0
s=1
fib=0
n=0
while n<inpooo:
    print(f)
    fib=f+s
    f=s
    s=fib
    n+=1

