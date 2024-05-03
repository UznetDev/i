def check(text: str) -> bool:
    for i in text:
        if text.count(i) > 1:
            return False
    return True

def substring(text: str) -> str:
    ln = len(text)
    res = ''
    for i in range(ln):
        for x in range(i+1, ln):
            r = text[i:x]
            if check(r) and len(r) > len(res):
                res = r
    return res

print(substring('ffgabnnkmm'))
print('fgabn')