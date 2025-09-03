# with arg and with return

def student(n,r,s1,s2,s3):
    print("name:",n)
    print("roll no:",r)
    a=s1+s2+s3
    return a

tot = student("Harika",15,99,98,90)
print("Total Marks:",tot)
print("Average Marks:", round(tot/3,3))

#=============================================================

#with no arg and with return

# def stu():
#     n = input("Enter name: ")
#     r= input("Enter roll number: ")
#     s1,s2,s3= map(int,input("Enter 3 subject marks: ").split())
#     tot = s1+s2+s3
#     return tot

# print("Total marks:" ,stu())