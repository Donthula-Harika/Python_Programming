#OPERATORS

def add(a,b):
    return a+b

def diff(a,b):
    if(a>b):
        return (a-b)
    else:
        return (b-a)
    
def mul(a,b):
    return a*b

def div(a,b):
    return a/b

def mod(a,b):
    return a%b



print("sum of 10 and 56 is:",add(10,56))
print("Difference between 6 and 9:" , diff(6,9))
print("Multiplication of 4 and 5 is:" , mul(4,5))
print("Division of 6 and 2 is:",div(6,2))
print("modulus of 11 and 3 is:",mod(11,3) )

print()
