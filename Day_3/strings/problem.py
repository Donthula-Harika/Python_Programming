#INPUT: aaabbca
# OUTPUT:a4b2c1

def cnt(x):
    l=[]
    for i in x:
        if i not in l:
            l.append(i)            
            cnt= x.count(i)
            print(f"{i}{cnt}",end="")
        



ip = input("Enter your input: ")
cnt(ip)