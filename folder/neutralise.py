
def neutralise(a: str, b: str):
    ln = len(a)
    text = ''
    for i in range(ln):
        if a[i] == b[i]:
            text += a[i]
        else:
            text += '0'
    return text


print(neutralise('+-+', '+--'))