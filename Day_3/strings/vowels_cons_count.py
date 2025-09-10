#tot no of vowels and consonents
def countvnc(s):
    vc=0
    cc=0
    for i in s:
        if i.lower() in["a","e","i","o","u"]:
            vc+=1
        else:
            if i.isalpha():
                cc+=1

    print(f"Vowels:{vc} \nConsonents: {cc}")



s="hello harika"
countvnc(s)
