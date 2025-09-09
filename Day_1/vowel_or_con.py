def check(a):
    if(a in ['a','e','i','o','u']):
        print(f"{a} is vowel")
    else:
        print(f"{a} i consonent")


c = input("Enter alphabet:").lower()
check(c)

