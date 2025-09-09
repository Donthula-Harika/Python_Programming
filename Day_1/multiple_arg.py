#convert days to years and months

def mul_arg(a,b,c):
    print(a,b,c)


mul_arg("hi",20,True)





def d_to_mandy(d):
    cm=0
    while(d>=365):
        y=d//365
        d=d%365
    
    while(d>=30):
        if(cm%2==0):
            m=d//30
            d=d%30
            cm+=1
        else:
            m=d//31
            d=d%30
            cm+=1


    print("Years:",y ,"months:",m ,"days:",d)

d_to_mandy(988)


