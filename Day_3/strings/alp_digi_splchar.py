#tot no.of alp,digits,spl char in string

def count(s):
    ca=0
    cd=0
    csc=0
    for i in s:
        print(i)
        if i.isalpha():
            ca+=1
        elif i.isdigit():
            cd+=1
        else:
            csc+=1

    print(f"Alphabets:{ca}, Digits: {cd}, Special characters: {csc}")



s="Heyy!!@123%*"
count(s)