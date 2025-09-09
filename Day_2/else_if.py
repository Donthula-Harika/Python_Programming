def week(n):
    if n==1:
        return "Sunday"
    elif n==2:
        return "Monday"
    elif n==3:
        return "Tuesday"
    elif n==4:
        return "wednesday"
    elif n==5:
        return "Thursday"
    elif n==6:
        return "Friday"
    elif n==7:
        return "Saturday"
    else:
        return "Invalid"
    
n = int(input("Enter week number:"))
print(week(n))