'''functions: self content block of statment
Types: in-buit n user-defined
2 imp things: fun definition and fun calling

'''

#fun with no arg n no return
def call1():
    print("\ncase1")
    print("No arg and no return")
    return 

#fun with arg and no return
def call2(a):
    print("\ncase2")
    print("with arg and no return")
    print("arg:",a )
    return 

#fun with arg and return
def call3(a):
    print("\ncase3")
    print("with arg and return")
    print("arg:",a )
    return 10

#fun with no arg and return
def call4():
    print("\ncase4")
    print("with no arg and return")
    return 10

print("returned",call1())
print("returned",call2(2))
print("returned",call3(10))
print("returned",call4())
