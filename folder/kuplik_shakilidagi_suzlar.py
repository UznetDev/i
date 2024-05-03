
def kuplik_shakilidagi_suzlar(lst: list):
    return [i+'s' if lst.count(i) > 1 else i for i in set(lst)]


data = ['cow', 'pig', 'cow', 'cow']
print(kuplik_shakilidagi_suzlar(data))

