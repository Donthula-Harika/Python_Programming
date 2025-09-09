#ascii char and their value
'''
65-90 ->A-Z
97-122 -> a-z
48-57 -> 0-9
'''


def ascii():
    for i in range(256):
        print(f"char:{chr(i)}  =>  val:{i}")

ascii()