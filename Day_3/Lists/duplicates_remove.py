#remove duplicates in list
def dup_count(l):
    
    l2 = []
    for num in l:
        if num not in l2:
           l2.append(num)
        
            
    
    print(f"List without dupicates:",l2)


l = [3,5,5,3,3,4]
dup_count(l)