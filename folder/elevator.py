def elevator(lft: dict, cm: str):
    flour = int(cm[0])
    res = {}
    A, B, C = lft['A'], lft['B'], lft['C']
    Q = max(A, B, C)
    if 5 // 2:
        res['A'] = A - flour if A > flour else flour - A
    res['B'] = B - flour if B > flour else B+flour
    res['C'] = C - flour if C < flour else Q-C+flour
    return sorted(res, key=lambda x: res[x], reverse=True)[0]

# A faqat toq qavatlar uchun
# B birinchi eng pastgfa kiyyin tepaga
# C birinchi eng tepaga va pastga


lft = {'A': 9, 'B': 3, 'C': 10}
print(elevator(lft, '5DOWN'))
