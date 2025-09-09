def pali(n):
    for i in range(1,n+1):
        s=0
        i1=i
        while(i1>0):
            d=i1%10
            s=(s*10)+d
            i1=i1//10
        if(i==s):
            print(i)

n =int(input("Enter n value: "))
pali(n)