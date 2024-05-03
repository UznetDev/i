#------------------------------------------------------   Set   -------------------------------------------------------|

# Ta'rifi:
# Set, o'zaro bir xil bo'lmagan elementlarni saqlash uchun ishlatiladi.
# Set lar tartiblanmagan va unikal elementlardan iborat.

# Mavzu bo'yicha ma'lumot:
# Setlar ko'p elementlarni saqlash uchun ishlatiladi,
# lekin ular ichidagi elementlar unikal bo'lishi kerak. Misol uchun: {1, 2, 3, 4, 5}.

# Farqlari:
# Set lar elementlarni o'zgartirishga qodir, ya'ni yangi elementlar qo'shish,
# o'chirish va elementlarni bir-biridan ajratib tashlashga imkoniyat beradi.
# Ular to'g'ri indekslanmagan va bir xil elementni yarim qolish mumkinligi yo'q.


# -----------------------------------------------  Dictionary method  -------------------------------------------------|


#------------------------------------------------------ clear() -------------------------------------------------------|
# clear(): Lug'atni tozalash uchun ishlatiladi.
# Qabul qiladigan qiymat: Yo'q.
# Qaytaradigan qiymat: Yo'q (None).
# Vazifa: Lug'atni tozalash.
# Xatolik: Yo'q.
my_dict = {'a': 1, 'b': 2, 'c': 3}
my_dict.clear()
print(my_dict)  # {}


#------------------------------------------------------- copy() -------------------------------------------------------|
# copy(): Lug'atning nusxasini olish uchun ishlatiladi.
# Qabul qiladigan qiymat: Yo'q.
# Qaytaradigan qiymat: Lug'atning nusxasi.
# Vazifa: Lug'atning nusxasini olish.
# Xatolik: Yo'q.
my_dict = {'a': 1, 'b': 2, 'c': 3}
new_dict = my_dict.copy()
print(new_dict)  # {'a': 1, 'b': 2, 'c': 3}


#----------------------------------------------------- fromkeys() -----------------------------------------------------|
# fromkeys(): Berilgan kalitlar uchun qiymatlar ro'yxatini yaratish uchun ishlatiladi.
# Qabul qiladigan qiymatlar: Kalitlar ro'yxati va boshlang'ich qiymat.
# Qaytaradigan qiymat: Yangi lug'at.
# Vazifa: Berilgan kalitlar uchun qiymatlar ro'yxatini yaratish.
# Xatolik: Yo'q.
keys = ['a', 'b', 'c']
values = 0
my_dict = dict.fromkeys(keys, values)
print(my_dict)  # {'a': 0, 'b': 0, 'c': 0}


#------------------------------------------------------- get() --------------------------------------------------------|
# get(): Berilgan kalit bo'yicha qiymatni olish uchun ishlatiladi.
# Qabul qiladigan qiymat: Kalit.
# Qaytaradigan qiymat: Berilgan kalit bo'yicha qiymat (agar mavjud bo'lsa), aks holda None.
# Vazifa: Berilgan kalit bo'yicha qiymatni olish.
# Xatolik: Yo'q.
my_dict = {'a': 1, 'b': 2, 'c': 3}
value = my_dict.get('b')
print(value)  # 2


#------------------------------------------------------ items() -------------------------------------------------------|
# items(): Lug'atning barcha juftliklarini olish uchun ishlatiladi.
# Qabul qiladigan qiymat: Yo'q.
# Qaytaradigan qiymat: Lug'atning juftliklarini ifodalovchi obyekt.
# Vazifa: Lug'atning barcha juftliklarini olish.
# Xatolik: Yo'q.
my_dict = {'a': 1, 'b': 2, 'c': 3}
items = my_dict.items()
print(items)  # dict_items([('a', 1), ('b', 2), ('c', 3)])


#------------------------------------------------------- keys() -------------------------------------------------------|
# keys(): Lug'atning barcha kalitlarini olish uchun ishlatiladi.
# Qabul qiladigan qiymat: Yo'q.
# Qaytaradigan qiymat: Lug'atning kalitlarini ifodalovchi obyekt.
# Vazifa: Lug'atning barcha kalitlarini olish.
# Xatolik: Yo'q.
my_dict = {'a': 1, 'b': 2, 'c': 3}
keys = my_dict.keys()
print(keys)  # dict_keys(['a', 'b', 'c'])


#------------------------------------------------------- pop() --------------------------------------------------------|
# pop(): Berilgan kalit bo'yicha qiymatni o'chirib tashlash uchun ishlatiladi.
# Qabul qiladigan qiymat: Kalit.
# Qaytaradigan qiymat: Berilgan kalit bo'yicha qiymat (agar mavjud bo'lsa).
# Vazifa: Berilgan kalit bo'yicha qiymatni o'chirib tashlash.
# Xatolik: Kalit mavjud emas bo'lsa KeyError qaytaradi.
my_dict = {'a': 1, 'b': 2, 'c': 3}
value = my_dict.pop('b')
print(value)  # 2


#----------------------------------------------------- popitem() ------------------------------------------------------|
# popitem(): Lug'atdan bir elementni olib tashlash uchun ishlatiladi.
# Qabul qiladigan qiymat: Yo'q.
# Qaytaradigan qiymat: Juftliklardan tasodifiy birini tuple ko'rinishida qaytaradi.
# Vazifa: Lug'atdan bir elementni olib tashlash.
# Xatolik: Lug'at bo'sh bo'lsa KeyError qaytaradi.
my_dict = {'a': 1, 'b': 2, 'c': 3}
item = my_dict.popitem()
print(item)  # ('c', 3)


#---------------------------------------------------- setdefault() ----------------------------------------------------|
# setdefault(): Berilgan kalit uchun qiymatni olish, agar kalit mavjud bo'lmasa, yangi qiymatni qo'shish uchun ishlatiladi.
# Qabul qiladigan qiymatlar: Kalit va boshlang'ich qiymat (agar mavjud bo'lmasa).
# Qaytaradigan qiymat: Kalit bo'yicha qiymat.
# Vazifa: Berilgan kalit bo'yicha qiymatni olish yoki qo'shish.
# Xatolik: Yo'q.
my_dict = {'a': 1, 'b': 2}
value = my_dict.setdefault('c', 3)
print(value)  #


