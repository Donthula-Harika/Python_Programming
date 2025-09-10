#add ele to list
def addEle(li,n):
    for i in range(n):
        e = input(f"Enter element {i+1}: ")
        li.append(e)
    print(li)

li=[]
n = int(input("Enter no of ele: "))
addEle(li,n)
