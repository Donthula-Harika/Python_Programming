def set_ope(s,e):
    s.add(e)



n = int(input("Enter no.of elements to add to a set: "))
s= set()
for i in range(n):
    e= int(input(f"enter element {i+1}:"))
    set_ope(s,e)
    

print(s)


