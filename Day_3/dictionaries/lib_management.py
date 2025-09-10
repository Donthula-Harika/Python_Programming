# You are building a Library Management System in Python. The system should store books in a dictionary where:

# Key → Book ID
# Value → Book Title
# Write a Python program to perform the following operations using Dictionaries:

# Add a book to the library (Book ID, Title).
# Remove a book using Book ID.
# Search for a book by Book ID and display the title.
# Update the title of a book (e.g., correction in title).
# Display all books in the library.
# Count the total number of books in the library.
# Check if a book title exists in the library (reverse lookup).

def add(d,b,t):
    d[b]=t
    print(d)

def remove(d,p):
    d.pop(p)
    print(d)

def search(d,p):
    if p in d:
        print("Found")
    else:
        print("Not found")

def update(d,k,v):
    d[k]=v

    
def display(d):
    for k,v in d.items():
        print(v,end=" ")
    print()
    

def count(d):
    print(f"Total products:", len(d))

def exist(d,t):
    if t in d.values():
        print("Found")
    else:
        print("Not found")






print("Operations:\n1.Add book\n2.Remove book\n3.Search boook\n4.update book\n5.display book\n6.count total books\n7.check if book title exist\n8.Exit")
d={}
while True:
    n = int(input("Enter your choice:"))
    
    if n==1:
        b=int(input("Enter book id: "))
        t=input("Enter book title: ")
        add(d,b,t)

    elif n==2:
        p = int(input("Enter book id1 to remove:"))
        remove(d,p)

    elif n==3:
        p = int(input("Enter book id to search:"))
        search(d,p)

    elif n==4:
        b= int(input("enter book id: "))
        t= input("enter title: ")
        update(d,b,t)

    elif n==5:
        display(d)

    elif n==6:
        count(d)

    elif n==7:
        t = input("enter book to check if it exist: ")
        exist(d,t)

    elif n==8:
        print("Exiting..")
        break

    else:
        print("invalid input")



