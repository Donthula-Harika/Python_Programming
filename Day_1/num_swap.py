#swaping numbers
a=int(input("Enter 'a' val:"))
b=int(input("Enter 'b' val:"))
print("Brfore swap:")
print("a:",a,"b:",b)

#using temp variable
t=a
a=b
b=t

print("After swap (using temp var):")
print("a:",a,"b:",b)


#without using temp variable
print("After swap (without using temp var):")

#m-1
a=a+b
b=a-b
a=a-b
print("a:",a,"b:",b)

#m-2
a,b=b,a
print("a:",a,"b:",b)


