def occ(s,c):
    ct=0
    for i in s:
        if i==c:
            ct+=1
    print(ct)

    #m-2
    cnt=s.count(c)
    print(cnt)


s="Hello Harikaa"
c =input("Enter a character:")
occ(s,c)
    
