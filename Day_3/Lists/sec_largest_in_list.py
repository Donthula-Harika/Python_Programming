def sec_larg(l):
    max1=l[0]
    max2=l[0]

    for i in range(1,len(l)):
        if l[i]>max1:
            max2=max1
            max1= l[i]
            
    print(max2)


l=[3,6,8,9,4,-1,10,89]
sec_larg(l)
