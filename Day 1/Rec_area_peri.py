
# l = int(input("Enter rectangle length: "))
# b = int(input("Enter rectangle breadth: "))

l,b = map(int,input("Enter length and breadth:").split())

print("Area:",l*b)
print("Circumference:", 2*(l+b))