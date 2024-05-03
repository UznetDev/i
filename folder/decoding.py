

def decoding(text: str, n: int, data: dict) ->str:
    for x in data:
        for i in text:
            if text.count(i) == data[x]:
                text = text.replace(i, x)
                break
    print(text)



print(decoding(text='?*!*!*', n=3, data={'b': 1, 'a': 3, 'n': 2}))