#tot duplicates count in list
def dup_count(l):
    c=0
    l2 = []
    for num in l:
        if num in l2:
            c+=1
        else:
            l2.append(num)
    
    print(f"Count:",c)


l = [3,5,5,3,3]
dup_count(l)
