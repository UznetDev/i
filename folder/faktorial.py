def get(x):
    res = 1
    for i in range(1, x+1):
        res *= i
    return res

def faktorial(n):
     for i in range(1, n):
         if get(i) == n:
             return True
         elif get(i) > n:
             return False


print(faktorial(24))

