def check(c):
    if c.isalpha():
        return "Alphabet"
    elif c.isdigit():
        return "Digit"
    else:
        return "Special character"
    
c=input("Enter a character: ")
print(check(c))