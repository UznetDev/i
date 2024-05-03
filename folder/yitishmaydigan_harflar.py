def yiotishmaydigan_harflar(text: str):
    res = ''
    for i in range(97, 123):
        s = chr(i)
        if s not in text:
            res += s
    return res


print(yiotishmaydigan_harflar('abs'))