print("Enter Student deatils")
st_num = input("Enter roll number:")
st_name = input("Enter name:")
s1,s2,s3= map(int,input("Enter 3 subject marks:").split())

tot_marks = s1+s2+s3


print("\nStudent Details: ")
print("Name:"+st_name+"\n"+"Roll_No:"+st_num )
print("Total marks:",tot_marks)
print("Average marks:",float(tot_marks//3))