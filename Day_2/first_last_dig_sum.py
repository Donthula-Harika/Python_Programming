def sum_string(n):
    s1= int(n[0])
    print(f"first digit:{s1}")
    s2= int(n[len(n)-1])
    print(f"last digit{s2}")
    s=s1+s2
    print(f"sum:{s}")
    

#m-2

def sum(n):
    n=int(n)
    s1=n%10
    # print(f"s1:{s1}")
    while(n>0):
        s=n%10
        n=n//10
        

    print(f"first digit:{s} \nlast digit:{s1}\nsum:{(s1+s)}")



n = input("Enter n value: ")
sum_string(n)
sum(n)
