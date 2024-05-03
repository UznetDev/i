from typing import List


def naqsh(color: List[str]) -> int:
    res = 0
    for i in range(1, len(color)):
        if color[i] != color[i - 1]:
            res += 1
        res += 2
    return res + 2

# test uchun
# print(naqsh(["Red", "Blue", "Red", "Blue", "Red"]))
# print(naqsh(["Blue"]))
# print(naqsh(["Red", "Yellow", "Green", "Blue"]))
# print(naqsh(["Blue", "Blue", "Blue", "Red", "Red", "Red"]))


print("Iltimos ranglarni kriting oxirida 'start' buyrug'ini kriting")
folder = []

while True:
    res = input(">>>    ")
    if res =='start':
        if folder:
            print(naqsh(folder))
        else:
            print('Ranglar mavjud emas.')
        break
    else:
        folder.append(res)