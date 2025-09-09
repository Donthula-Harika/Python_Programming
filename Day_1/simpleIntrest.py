p = int(input("Enter principle amount:"))
r = int(input("Enter Rate of Interest:"))
t = int(input("Enter total no.of months:"))

#Simple Interest
s= (p*t*r)//100
print("Simple Interest is", s)
print("Amount in hand is ",s+p )