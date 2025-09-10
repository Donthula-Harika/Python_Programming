# Prog too search all occurences of a character in a given string

def search_occ(s,c):
    for i in range(len(s)):
        if s[i]==c:
            print(f"occured at index:{i}")


s="hello harikaa"
c =input("Enter a character:")
search_occ(s,c)
    