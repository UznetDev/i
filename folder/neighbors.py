

def neighbors(lst: list):
    ln = len(lst)
    for i in range(ln-1):
        if lst[i]-lst[i+1]==1 or lst[i+1]-lst[i]==1:
            print(lst[i], lst[i+1])



lst = [-1, 2, 3, -1, -2]
print(neighbors(lst))
