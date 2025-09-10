#print all unique elements in list


def uni_ele(l):
    unique = []
    for num in l:
        if l.count(num) == 1:
            unique.append(num)
    print("Unique elements are:", unique)

l = [3, 3, 57, 8, 4, 3, 46, 6, 9]
uni_ele(l)

