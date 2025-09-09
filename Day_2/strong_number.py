#strong number: 145 -> 1!+4!+5! = 145

def fact(n):
    p=1
    while(n>0):
        p=p*n
        n=n-1
    return p

def strong_num(n):
    for i in range(1,n+1):
        s=0
        i1=i
        while(i1>0):
            d=i1%10
            s=s+fact(d)
            i1=i1//10
        if(i==s):
            print(i)


n = int(input("Enter n value:"))
strong_num(n)

