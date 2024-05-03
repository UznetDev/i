def qsort(arr):
    ln = len(arr)
    if ln<2:
        return arr
    else:
        midle = arr.pop(ln//2)
        mini_arr = [i for i in arr if i<=midle]
        max_arr = [i for i in arr if i>midle]
        return qsort(mini_arr) + [midle] + qsort(max_arr)