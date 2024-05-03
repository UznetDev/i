from typing import List


def labirint(lst: List[List[int]]) -> bool:
    row_end = 5
    colum_end = 7
    if lst[row_end-1][colum_end-1]:
        return False
    def func(lst: List[List[int]], row_start=0, colum_start=0) -> bool:
        row_end = 4
        colum_end = 6
        if row_start==row_end and colum_start==colum_end:
            return True
        elif colum_start<colum_end and lst[row_start][colum_start+1] == 0:
            return func(lst, row_start, colum_start+1)
        elif row_start<row_end and lst[row_start+1][colum_start] == 0:
            return func(lst, row_start+1, colum_start)
        # elif row_start and lst[row_start-1][colum_start] == 0:
        #     return func(lst, row_start-1, colum_start)
        # elif colum_start and lst[row_start][colum_start-1] == 0:
        #     return func(lst, row_start, colum_start-1)
        else:
            return False
    return func(lst)



test1 = [[0, 1, 1, 1, 1, 1, 1],
         [0, 0, 1, 1, 0, 1, 1],
         [1, 0, 0, 0, 0, 1, 1],
         [1, 1, 1, 1, 0, 0, 1],
         [1, 1, 1, 1, 1, 0, 0]]

test2  =[[0, 1, 1, 1, 1, 1, 1],
         [0, 0, 1, 0, 0, 1, 1],
         [1, 0, 0, 0, 0, 1, 1],
         [1, 1, 0, 1, 0, 0, 1],
         [1, 1, 0, 0, 1, 1, 1]]

test3 = [[0, 1, 1, 1, 1, 0, 0],
         [0, 0, 0, 0, 1, 0, 0],
         [1, 1, 1, 0, 0, 0, 0],
         [1, 1, 1, 1, 1, 1, 0],
         [1, 1, 1, 1, 1, 1, 1]]

test4 = [[0, 1, 1, 1, 1, 0, 0],
         [0, 0, 0, 0, 1, 0, 0],
         [1, 1, 1, 0, 0, 0, 0],
         [1, 0, 0, 0, 1, 1, 0],
         [1, 1, 1, 1, 1, 1, 0]]

print(labirint(test1))
print(labirint(test2))
print(labirint(test3))
print(labirint(test4))
