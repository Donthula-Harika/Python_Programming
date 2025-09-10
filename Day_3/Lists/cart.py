# You are building a simple E-commerce application in python. The system should maintain a list of products available in the cart. Write a python program to perform the following operations using lists:
# Add a product to the cart
# Remove a product from the cart
# Search for a product in the cart
# Display all products in the cart
# Count number of products in the cart

def add(l,p):
    l.append(p)
    print(l)

def remove(l,p):
    l.remove(p)
    print(l)

def search(l,p):
    if p in l:
        print("Found")
    else:
        print("Not found")
    
def display(l):
    print(l)

def count(l):
    print(f"Total products:", len(l))

def sort(l):
    l.sort()

def clear(l):
    l.clear()



print("Cart Operations:\n1.Add product\n2.Remove product\n3.Search Product\n4.Display cart\n5.Count Products\n6.sort\n7.clear\n8.Exit")
l=['car']
while True:
    n = int(input("Enter your choice:"))
    
    if n==1:
        p=input("Enter product to add:")
        add(l,p)

    elif n==2:
        p = input("Enter product to remove:")
        remove(l,p)

    elif n==3:
        p = input("Enter product to search:")
        search(l,p)

    elif n==4:
        display(l)

    elif n==5:
        count(l)

    elif n==6:
        sort(l)

    elif n==7:
        clear(l)

    elif n==8:
        print("Exiting..")
        break

    else:
        print("invalid input")




