def high_freq_char(x):
    l=[]
    char=[]
    max=0
    for i in x:
        if i not in l:
            l.append(i)            
            cnt= x.count(i)
            if cnt>=max:
                max=cnt
                char.append(i)

    
    print(char)

s="hello harika"
high_freq_char(s)