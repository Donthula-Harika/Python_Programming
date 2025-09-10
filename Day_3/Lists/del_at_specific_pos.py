#del ele from specific pos

#with pop()
def del_pos_m1(l,pos):
    l.pop(pos)
    print(l)

#without pop()
def del_pos_m2(l,pos):
    lst=[]
    for i in range(len(l)):
        if i!=pos:
            lst=lst+ [l[i]]
    print(lst)


l = [2,4,6,7]
n = int(input("Position to delete:"))
del_pos_m1(l,n)
del_pos_m2(l,n)