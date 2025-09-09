#fibonacci

def fib(n):
    f=0
    s=1
    print(f,s,end=" ")
    for i in range(3,n+1):
        t=f+s
        f=s
        s=t
        print(t,end=" ")

n=int(input("enter n value"))
fib(n)

