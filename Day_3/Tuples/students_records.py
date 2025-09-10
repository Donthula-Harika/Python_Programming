# A school stores student records as tuples in the format (roll_no, name, marks) Write a python program to:
# Store the data of 5 students in a list of tuples
# Print the name of the student who scored the highest marks
# Print all students who scored more than 75 marks

def stu(l):

    print("All student records:", l)

    # Student with highest marks
    top_student = l[0]  
    for student in l[1:]:
        if student[2] > top_student[2]:
            top_student = student

    print(f"Student with highest marks: {top_student[1]} ({top_student[2]} marks)")

    #complete stu with marks>75
    
    l2=[]
    for j in range(n):
        if l[j][2]>75:
            l2.append(l[j][1])
            
    print(f"stu with marks>75: {l2}")



n = 5
students_list=[]
for i in range(n):
    r,na,m = input("Enter student {i+1} roll no, name, marks:").split()
    students_list.append((r,na,int(m)))

stu(students_list)
