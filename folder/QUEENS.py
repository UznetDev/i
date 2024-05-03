
def check(row, col, lst: list[list[int]]) -> bool:
    for i in range(0, 8):
        if i != row and lst[i][col]:
            return False
    for i in range(0, 8):
        if i != col and lst[row][i]:
            return False
    for i in range(0, 8):
        if ((col-i >= 0 and row+i < 8 and lst[row+i][col-i] and col-i != col and row+i != row) or
                (row-i >= 0 and col+i < 8 and lst[row-i][col+i] and col+i != col and row-i != row)):
            return False
    for i in range(1, 8):
        if ((col+i < 8 and row+i < 8 and lst[row+i][col+i]) or
                (col-i >= 0 and row-i >= 0 and lst[row-i][col-i])):
            return False
    return True



doska = [[0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0]]

kordinata1 = [[1, 8],
             [2, 7],
             [3, 6],
             [4, 5],
             [5, 4],
             [6, 3],
             [7, 2],
             [8, 1]]

kordinata = [[1, 7],
             [2, 4],
             [3, 2],
             [4, 8],
             [5, 6],
             [6, 1],
             [7, 3],
             [8, 5]]

for i in kordinata:
    doska[i[0]-1][i[1]-1] = 1

for i in kordinata:
    if not check(row=i[0]-1, col=i[1]-1, lst=doska):
        print('NO')
        exit()

print('OK')

for i in doska:
    print(i)