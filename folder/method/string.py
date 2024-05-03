# -----------------------------------------------------  String   -----------------------------------------------------|

# Ta'rifi:
# String, belgilar yig'indisi, ya'ni matnlar uchun ishlatiladi.
# Matnning har bir belgisi alohida belgi (harf, raqam, belgilarni ko'rsatuvchi belgilar va h.k.) bo'lishi mumkin.

# Mavzu bo'yicha ma'lumot:
# Stringlar Python dasturlash tili ichidagi eng mashhur ma'lumot turi.
# Ularning ichidagi belgilar o'zgarmasdir va to'g'ri chiziqli qo'shish bilan hosil bo'ladi.
# Misol uchun: "Hello, world!", '12345', yoki 'Python rocks!'.

# Farqlari:
# Stringlar o'zgarmasdir, ya'ni ularning ichidagi belgilar o'zgartirib bo'lmaydi.
# Matnlarni yig'ish (+ operatori orqali),
# ko'paytirish (* operatori orqali) va ko'rsatish (indexlar orqali) mumkin.


# --------------------------------------------------  string method  --------------------------------------------------|


# -----------------------------------------------------capitalize()-----------------------------------------------------|
string = "Bu bir misol matni"
# capitalize(): Stringni bosh harf bilan boshlang'ich harfga o'zgartiradi.
# Xatolik: Yo'q.
print(string.capitalize())  # "Bu bir misol matni"

# ------------------------------------------------------casefold()------------------------------------------------------|
string = "Bu bir misol matni"
# casefold(): Stringni kichik harflarga o'zgartiradi.
# Xatolik: Yo'q.
print(string.casefold())  # "bu bir misol matni"

# ----------------------------------------------------center(width)-----------------------------------------------------|
string = "Bu bir misol matni"
# center(width): Stringni belgilangan uzunlikda qo'shish belgisi bilan markazlashadi.
# Xatolik: Yo'q.
print(string.center(30, '*'))  # "***Bu bir misol matni****"

# ---------------------------------------------------count(substring)---------------------------------------------------|
string = "Bu bir misol matni"
# count(substring): Stringda berilgan qatorning necha marta paydo bo'ldigini hisoblaydi
# agar topilmasa 0 qaytaradi.
# Xatolik: Yo'q.
print(string.count('i'))  # 2

# ---------------------------------------------------encode(encoding)---------------------------------------------------|
string = "Bu bir misol matni"
# encode(encoding): Stringni berilgan kodlashuvda kodlaydi.
# Xatolik: Encoding xatoliklari mumkin.
print(string.encode())  # b'Bu bir misol matni'

# ---------------------------------------------------endswith(suffix)---------------------------------------------------|
string = "Bu bir misol matni"
# endswith(suffix): Matn berilgan oxirgi substring bilan tugaganda True, aks holda False qaytaradi..
# Xatolik: Yo'q.
print(string.endswith('matni'))  # True

# -------------------------------------------------expandtabs(tabsize)--------------------------------------------------|
string = "Bu bir misol matni"
# expandtabs(tabsize): Tablitsa belgisini belgilangan o'lchovga mosligicha ko'paytiradi.
# Xatolik: Yo'q.
print('Bu\tbir\tmisol\tmatni'.expandtabs())  # "Bu      bir     misol   matni"

# ---------------------------------------------------find(substring)----------------------------------------------------|
string = "Bu bir misol matni"
# find(substring): Berilgan qatorni stringda qidiradi va uning birinchi indeksini qaytaradi. Agar topilmasa,
# -1 qaytaradi.
# Xatolik: Yo'q.
print(string.find('misol'))  # 7

# -------------------------------------------------------format()-------------------------------------------------------|
string = "Bu bir misol matni"
# format(): Formatlash uchun ishlatiladi.
# Xatolik: Yo'q.
print("Misol: {}".format(string))  # "Misol: Bu bir misol matni"

# -------------------------------------------------format_map(mapping)--------------------------------------------------|
string = "Bu bir misol matni"
# format_map(mapping): Formatlash uchun ishlatiladi.
# Xatolik: Yo'q.
print("Misol: {str}".format_map({'str': string}))  # "Misol: Bu bir misol matni"

# ---------------------------------------------------index(substring)---------------------------------------------------|
string = "Bu bir misol matni"
# index(substring): find() metodiga o'xshash, ammo topilmaganda xato qaytaradi.
# Xatolik: ValueError.
print(string.index('bir'))  # 3

# ------------------------------------------------------isalnum()-------------------------------------------------------|
string = "Bu bir misol matni"
# isalnum(): String faqat alfanumerik belgilar (raqamlar va harflar)dan iborat bo'lsa True qaytaradi.
# Xatolik: Yo'q.
print(string.isalnum())  # False

# ------------------------------------------------------isalpha()-------------------------------------------------------|
string = "Bu bir misol matni"
# isalpha(): String faqat harflardan iborat bo'lsa True qaytaradi.
# Xatolik: Yo'q.
print(string.isalpha())  # False

# ------------------------------------------------------isascii()-------------------------------------------------------|
string = "Bu bir misol matni"
# isascii(): String faqat ASCII belgilardan iborat bo'lsa True qaytaradi.
# Xatolik: Yo'q.
print(string.isascii())  # True

# -----------------------------------------------------isdecimal()------------------------------------------------------|
string = "Bu bir misol matni"
# isdecimal(): String faqat sonlar bo'lsa True qaytaradi.
# Xatolik: Yo'q.
print(string.isdecimal())  # False

# ------------------------------------------------------isdigit()-------------------------------------------------------|
string = "Bu bir misol matni"
# isdigit(): String faqat raqamlar bo'lsa True qaytaradi.
# Xatolik: Yo'q.
print(string.isdigit())  # False

# ----------------------------------------------------isidentifier()----------------------------------------------------|
string = "Bu bir misol matni"
# isidentifier(): String Pythonda identifikator bo'lsa True qaytaradi.
# Xatolik: Yo'q.
print(string.isidentifier())  # False

# ------------------------------------------------------islower()-------------------------------------------------------|
string = "Bu bir misol matni"
# islower(): String faqat kichik harflardan iborat bo'lsa True qaytaradi.
# Xatolik: Yo'q.
print(string.islower())  # False

# -----------------------------------------------------isnumeric()------------------------------------------------------|
string = "Bu bir misol matni"
# isnumeric(): String faqat sonlar bo'lsa True qaytaradi.
# Xatolik: Yo'q.
print(string.isnumeric())  # False

# ----------------------------------------------------isprintable()-----------------------------------------------------|
string = "Bu bir misol matni"
# isprintable(): String chiqarilishi mumkin bo'lsa True qaytaradi.
# Xatolik: Yo'q.
print(string.isprintable())  # True

# ------------------------------------------------------isspace()-------------------------------------------------------|
string = "Bu bir misol matni"
# isspace(): String faqat bo'shliklardan iborat bo'lsa True qaytaradi.
# Xatolik: Yo'q.
print(string.isspace())  # False

# ------------------------------------------------------istitle()-------------------------------------------------------|
string = "Bu bir misol matni"
# istitle(): Stringning har bir so'zi bosh harf bilan boshlanib, qolgan harflar kichik bo'lsa True qaytaradi.
# Xatolik: Yo'q.
print(string.istitle())  # False

# ------------------------------------------------------isupper()-------------------------------------------------------|
string = "Bu bir misol matni"
# isupper(): String faqat katta harflardan iborat bo'lsa True qaytaradi.
# Xatolik: Yo'q.
print(string.isupper())  # False

# ----------------------------------------------------join(iterable)----------------------------------------------------|
string = "Bu bir misol matni"
# join(iterable): Iterable bo'lsa, stringning barcha elementlarini bir qatorga biriktiradi.
# Xatolik: Yo'q.
print('-'.join(['Bu', 'bir', 'misol', 'matni']))  # "Bu-bir-misol-matni"

# -----------------------------------------------------ljust(width)-----------------------------------------------------|
string = "Bu bir misol matni"
# ljust(width): Stringni belgilangan uzunlikda chap tomondan to'ldiradi.
# Xatolik: Yo'q.
print(string.ljust(30, '-'))  # "Bu bir misol matni--------"

# -------------------------------------------------------lower()--------------------------------------------------------|
string = "Bu bir misol matni"
# lower(): Stringni kichik harflarga o'zgartiradi.
# Xatolik: Yo'q.
print(string.lower())  # "bu bir misol matni"

# -------------------------------------------------------lstrip()-------------------------------------------------------|
string = "Bu bir misol matni"
# lstrip(): Chap tomondagi bo'shliqlarni olib tashlaydi.
# Xatolik: Yo'q.
print("   Bu bir misol matni".lstrip())  # "Bu bir misol matni"

# --------------------------------------------------maketrans(x, y, z)--------------------------------------------------|
string = "Bu bir misol matni"
# maketrans(x, y, z): Stringni almashtirish uchun harflarni, alifbo indexini,
# yoki ikkita belgining orasidagi almashuvlar ro'yxatini yaratadi.
# Xatolik: Yo'q.
translation_table = str.maketrans('Bu', 'Yu')
print(string.translate(translation_table))  # "Yu bir misol matni"

# -------------------------------------------------partition(separator)-------------------------------------------------|
string = "Bu bir misol matni"
# partition(separator): Stringni separator bilan ajratib o'ng tomonini ko'rsatadi.
# Xatolik: Yo'q.
print(string.partition('bir'))  # ('Bu ', 'bir', ' misol matni')

# --------------------------------------------------replace(old, new)---------------------------------------------------|
string = "Bu bir misol matni"
# replace(old, new): Stringdagi eski belgilarni yangi belgilarga o'zgartiradi.
# Xatolik: Yo'q.
print(string.replace('misol', 'namuna'))  # "Bu bir namuna matni"

# ---------------------------------------------------rfind(substring)---------------------------------------------------|
string = "Bu bir misol matni"
# rfind(substring): find() metodiga o'xshash, ammo stringni oxiridan boshlab qidiradi.
# Xatolik: Yo'q.
print(string.rfind('i'))  # 13

# --------------------------------------------------rindex(substring)---------------------------------------------------|
string = "Bu bir misol matni"
# rindex(substring): index() metodiga o'xshash, lekin so'nggi topilgan indeksni qaytaradi.
# Agar topilmasa ValueError qaytaradi.
# Xatolik: ValueError.
print(string.rindex('i'))  # 13

# -----------------------------------------------------rjust(width)-----------------------------------------------------|
string = "Bu bir misol matni"
# rjust(width): Stringni belgilangan uzunlikda o'ng tomondan to'ldiradi.
# Xatolik: Yo'q.
print(string.rjust(30, '-'))  # "--------Bu bir misol matni"

# ------------------------------------------------rpartition(separator)-------------------------------------------------|
string = "Bu bir misol matni"
# rpartition(separator): Stringni separator bilan ajratib chap tomonini ko'rsatadi.
# Xatolik: Yo'q.
print(string.rpartition('bir'))  # ('Bu ', 'bir', ' misol matni')

# --------------------------------------------------rsplit(separator)---------------------------------------------------|
string = "Bu bir misol matni"
# rsplit(separator): Stringni separator bo'yicha bo'lib qismalaydi, ammo chapdan o'ngga qidiradi.
# Xatolik: Yo'q.
print(string.rsplit(' '))  # ['Bu', 'bir', 'misol', 'matni']

# -------------------------------------------------------rstrip()-------------------------------------------------------|
string = "Bu bir misol matni"
# rstrip(): O'ng tomondagi bo'shliqlarni olib tashlaydi.
# Xatolik: Yo'q.
print("Bu bir misol matni   ".rstrip())  # "Bu bir misol matni"

# ---------------------------------------------------split(separator)---------------------------------------------------|
string = "Bu bir misol matni"
# split(separator): Stringni separator bilan bo'lib qismalaydi.
# Xatolik: Yo'q.
print(string.split(' '))  # ['Bu', 'bir', 'misol', 'matni']

# -----------------------------------------------------splitlines()-----------------------------------------------------|
string = "Bu bir misol matni"
# splitlines(): Stringni qatorlarga bo'lib qismalaydi.
# Xatolik: Yo'q.
multiline_string = "Bu bir misol matni\nVa boshqa qator\nSo'nggi qator"
print(multiline_string.splitlines())  # ['Bu bir misol matni', 'Va boshqa qator', "So'nggi qator"]

# --------------------------------------------------startswith(prefix)--------------------------------------------------|
string = "Bu bir misol matni"
# startswith(prefix): String belgilangan so'z bilan boshlansa, True qaytaradi.
# Xatolik: Yo'q.
print(string.startswith('Bu'))  # True

# -------------------------------------------------------strip()--------------------------------------------------------|
string = "Bu bir misol matni         "
# strip(): Chap va o'ng tomondagi bo'shliqlarni olib tashlaydi.
# Xatolik: Yo'q.
print(string.strip())  # "Bu bir misol matni"

# ------------------------------------------------------swapcase()------------------------------------------------------|
string = "Bu bir misol matni"
# swapcase(): Kichik harflarni katta, katta harflarni kichikga o'zgartiradi.
# Xatolik: Yo'q.
print(string.swapcase())  # "bU BIR MISOL MATNI"

# -------------------------------------------------------title()--------------------------------------------------------|
string = "Bu bir misol matni"
# title(): Stringni juda to'g'ri formatlash uchun ishlatiladi.
# Xatolik: Yo'q.
print(string.title())  # "Bu Bir Misol Matni"

# -------------------------------------------------------upper()--------------------------------------------------------|
string = "Bu bir misol matni"
# upper(): Stringni katta harflarga o'zgartiradi.
# Xatolik: Yo'q.
print(string.upper())  # "BU BIR MISOL MATNI"

# -----------------------------------------------------zfill(width)-----------------------------------------------------|
string = "Bu bir misol matni"
# zfill(width): Stringni berilgan uzunlikka teng bo'lgan qilib, boshidan nol qo'shadi.
# Xatolik: Yo'q.
print(string.zfill(30))  # "0000000000000Bu bir misol matni"