def ntow(n):
    words=""
    while(n>0):
        d = n%10
        n=n//10
        w=["zero","one","two","three","four","five","six","seven","eight","nine"]
        words=w[d]+" "+words

    print(words)


n = int(input("Enter n value: "))
ntow(n) 