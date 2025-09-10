#find lenght of string without using len()
#concatenate 2 strings
def length(s):
    c=0
    for i in s:
        c+=1
    print("Concatenated string is:",c)

def concate(a,b):
    print("Length of the string is:",a+b)

def compare(s1,s2):
    return s1==s2


s="Hello Welcome"
length(s)

s1="hello "
s2="World"
s3="hello "
concate(s1,s2)
print(compare(s1,s2))
print(compare(s1,s3))

