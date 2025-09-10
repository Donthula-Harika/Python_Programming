# Count freq of each ele

def count_frequency(lst):
    unique = []
    freq = []

    for num in lst:
        if num in unique:
            index = unique.index(num)
            freq[index] += 1
        else:
            unique.append(num)
            freq.append(1)
    
    for i in range(len(unique)):
        print(f"{unique[i]}->{freq[i]}")


lst = [10, 5, 10, 3, 5, 10]
count_frequency(lst)
