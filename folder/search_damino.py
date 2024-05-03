from typing import List


def lst_to_f(lst):
    return float('.'.join([str(i) for i in lst]))

def sort(arr):
    ln = len(arr)
    if ln<2:
        return arr
    else:
        midle = arr.pop(ln//2)
        mini_arr = [i for i in arr if lst_to_f(i)<=lst_to_f(midle)]
        max_arr = [i for i in arr if lst_to_f(i)>lst_to_f(midle)]
        return sort(mini_arr) + [midle] + sort(max_arr)


def search_damino(lst: List[List[int]]) -> bool:
    damino = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [1, 1], [1, 2],
              [1, 3], [1, 4], [1, 5], [1, 6], [2, 2], [2, 3], [2, 4], [2, 5], [2, 6],
              [3, 3], [3, 4], [3, 5], [3, 6], [4, 4], [4, 5], [4, 6], [5, 5], [5, 6], [6, 6]]
    start = 0
    end = len(lst)
    folder = []
    for i in range(len(lst)):
        if lst[i][0] > lst[i][1]:
            lst[i] = lst[i][::-1]
    lst = sort(lst)
    for i in damino:
        if end>start and lst[start] == i and lst[start] == i:
            start += 1
        else:
            folder.append(i)
    return folder



val = [[0, 0], [0, 1], [0, 5], [1, 1], [1, 3], [1, 6], [2, 2], [2, 6], [3, 5],
       [4, 1], [4, 4],[4, 5], [4, 6], [5, 1], [5, 2], [5, 5], [6, 0], [6, 3]]

print(search_damino(val))