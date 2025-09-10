#count tot no.of even and odd ele in list
def count(li):
    ec=0
    oc=0
    for i in li:
        if(i%2==0):
            ec+=1
        else:
            oc+=1
    print(f"Even elements count:{ec}")
    print(f"odd elements count:{oc}")

li=[2,3,5,7,8,1,4]
count(li)
