def check(text: str) -> bool:
    for i in text:
        if text.count(i) > 1:
            return False
    return True


def file_manager(file_path: str) -> str:
    res = ''
    with open(file_path, 'r') as f:
        text= f.read().split()
        for i in text:
            ln = len(i)
            ln = (ln if ln//2==0 else ln + 1) // 2
            r = f"{i[ln:]}{i[:ln]}"
            if check(r):
                res += r+'\n'
    return res

print(file_manager('file.txt'))
