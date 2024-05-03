from typing import List


def dublicate_zeros(lst: List[int]) -> List:
    i = 0
    while i < len(lst):
        if lst[i] == 0:
            lst.insert(i+1, 0)
            i+=2
        else:
            i += 1
    return lst

print(dublicate_zeros([1, 0, 2, 3, 0, 4, 5, 0])==[1, 0, 0, 2, 3, 0, 0, 4, 5, 0, 0 ])