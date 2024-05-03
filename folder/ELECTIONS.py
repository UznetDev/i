

def sort(lst: list, func=lambda x: x):
    ln = len(lst)
    if ln < 2:
        return lst
    middle = list(lst).pop(ln//2)
    right = [i for i in lst if func(i) < func(middle)]
    left = [i for i in lst if func(i) > func(middle)]
    return sort(left, func) + [middle] + sort(right, func)



with open('file.txt', 'r') as f:
    data = {}
    count = 0
    for i in f.read().split():
        if i in data:
            data[i] += 1
        else:
            data[i] = 1
        count+=1
    # print(data, (count/100)*50)
    res = sort(data, func=lambda x: data[x])
    print(res, data)
    for i in range(2):
        if data[res[i]] > count/100*50:
            print(res[i])
            break
        print(res[i])

