'''
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
'''  

def pattern(n):
    for i in range(n):
        for j in range(n):
            print("* ",end="")
        print()

n = int(input("enter n value:"))

pattern(n)