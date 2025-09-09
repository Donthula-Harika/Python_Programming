def fact(n):
    n1=n
    p=1
    while(n>0):
        p=p*n
        n=n-1
    print(f"factorial of {n1} is {p}")

def show(n):
    s=""
    while(n>0):
        if(n==1):
            s=s+""+str(n)
        else:
            s=s+"*"+str(n)
        n-=1
    print(s)

n = int(input("Enter n value: "))
fact(n)
show(n)