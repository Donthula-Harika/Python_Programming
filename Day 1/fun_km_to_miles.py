#KM to Miles with arg and with return
# def kmtomiles(a):
#     miles = 0.62*a
#     return miles

# km= int(input("Enter km:"))
# print("In miles:", kmtomiles(km))

#KM to Miles without arg and without return
def km_to_miles():
    a=int(input("Enter km:"))
    print("In kilometers:",a)
    miles= a*0.6213
    print("In miles:",round(miles,3))

km_to_miles()

