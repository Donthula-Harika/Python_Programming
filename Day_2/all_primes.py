def prime(n):
    for j in range(1,n+1):
        i=1
        c=0
        while(i<j):
            if(j%i==0):
                c=c+1
            i=i+1
            
        if(c==1):
            print(j)
        




n = int(input("Enter n value: "))
prime(n)