#Student Pass or Fail and grade
def student(n,r,s1,s2,s3):
    print("name:",n)
    print("roll no:",r)
    t=(s1+s2+s3)//3
    print("Avg:",t)

    if (t>=40):
        if t<=50:
            return "C grade"
        elif t<=70:
            return "B grade"
        elif t<=80:
            return "A grade"
        else:
            return "Distension"
    else:
        return "Fail"



print("Enter Student deatils")
st_num = input("Enter roll number:")
st_name = input("Enter name:")
s1,s2,s3= map(int,input("Enter 3 subject marks:").split())
print("Grade is",student(st_name,st_num,s1,s2,s3))


