def prime(n):
    i=2
    c=0
    while(i<n):
        if(n%i==0):
            c=c+1
        i=i+1
        
    if(c==0):
        return True
    else:
        return False

def factors(n):
    for i in range(1,n+1):
        if(n%i==0 and prime(i)):
            print(i,end=" ")


n = int(input("Enter n value: "))
factors(n)
