#perfect number

def pn(n):
    for i in range(1,n+1):
        s=0
        for j in range(1,i):
            if(i%j==0):
                s+=j
        # print("sum:",s)
        if(i==s):
            print(i)




n = int(input("Enter n value: "))
pn(n)