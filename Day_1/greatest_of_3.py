def greater(a,b,c):
    if(a>b):
        if(a>c):
            print(f"{a} is greater")
        else:
            print(f"{c} is greater")
    else:
        if(b>c):
            print(f"{b} is greater")
        else:
            print(f"{c} is greater")

greater(10,101,12)