# def arm(n):
#     for i in range(1,n+1):
#         i=str(i)
#         k=0
#         for j in range(len(i)-1):
#             k+=int(i[j])**3
        

#         if(i==k):
#             print(i)


def armst(n):
    for i in range(1,n+1):
        s=0
        i1=i
        while(i1>0):
            d=i1%10
            s=s+d**3
            i1=i1//10
        if(i==s):
            print(i)


n = int(input("Enter n value:"))
armst(n)