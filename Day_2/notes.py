def notes_count(a):
    while(a>0):
        c=0
        if a>=2000: 
            t= a//2000
            a=a-(2000*t)
            c+=t
        elif a>=500:
            t = a//500
            a=a-(500*t)
            c+=t
        elif a>=50:
            t = a//50
            a=a-(20*t)
            c+=t
        elif(a>=10):
            t=a//10
            a=a-(10*t)
            c+=t
        
        else:
            t=a//10
            a=a-(10*t)
            c+=t

    print("Notes :", c)

amt =int(input("Enter amount: "))
notes_count(amt)