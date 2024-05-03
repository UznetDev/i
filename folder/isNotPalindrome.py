
def isNotPalindrome(num):
    return not str(num) == str(num)[::-1]

# test uchun
# print(isNotPalindrome(6090609))
# print(isNotPalindrome(9669))
# print(isNotPalindrome(69069069))
# print(isNotPalindrome(69))

try:
    print(isNotPalindrome(int(input(">>>    "))))
except:
    print('Xato qiymat kritildi')