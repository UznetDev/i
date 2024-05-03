#-------------------------------------------------------  List  -------------------------------------------------------|

# Ta'rifi:
# List, o'zgaruvchan, tartiblangan elementlarni saqlash uchun ishlatiladi.
# Elementlar ro'yxat bo'yicha tartiblangan holda saqlanadi va har qanday turdagi obyektlarni o'z ichiga oladi.

# Mavzu bo'yicha ma'lumot:
# Listlar ko'p elementlarni o'z ichiga oladi va bu elementlar tartiblangan holda saqlanadi.
# Misol uchun: [1, 2, 3, 4, 5], ['apple', 'banana', 'cherry'], yoki [1, 'apple', True, 3.14].

# Farqlari:
# Listlar o'zgartirish mumkin, ya'ni yangi elementlar qo'shish, elementlarni o'chirish,
# yoki elementlarni o'zgartirish uchun maslahatlar beradi.
# List elementlariga indeks orqali murojat qilish, massivlar ustida matematik amallar bajaratish mumkin.


#----------------------------------------------------  List method ----------------------------------------------------|


#-------------------------------------------------------append()-------------------------------------------------------|
# append(): Ro'yxatga yangi bir elementni qo'shish uchun ishlatiladi.
# Qabul qiladigan qiymat: Qo'shiladigan element.
# Qaytaradigan qiymat: Yo'q (None).
# Error: Yo'q.
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # [1, 2, 3, 4]

#-------------------------------------------------------clear()--------------------------------------------------------|
# clear(): Ro'yxatni tozalash uchun ishlatiladi.
# Qabul qiladigan qiymat: Yo'q.
# Qaytaradigan qiymat: Yo'q.
# Error: Yo'q.
my_list = [1, 2, 3]
my_list.clear()
print(my_list)  # []

#--------------------------------------------------------copy()--------------------------------------------------------|
# copy(): Ro'yxatni nusxasini olish uchun ishlatiladi.
# Qabul qiladigan qiymat: Yo'q.
# Qaytaradigan qiymat: Ro'yxatning nusxasi.
# Error: Yo'q.
my_list = [1, 2, 3]
new_list = my_list.copy()
print(new_list)  # [1, 2, 3]

#-------------------------------------------------------count()--------------------------------------------------------|
# count(): Berilgan elementning ro'yxatda necha marta paydo bo'ldigini hisoblash uchun ishlatiladi.
# Qabul qiladigan qiymat: Hisoblanadigan element.
# Qaytaradigan qiymat: Elementning ro'yxatda paydo bo'lgan ko'paytmasi.
# Error: Yo'q.
my_list = [1, 2, 2, 3, 4, 2]
print(my_list.count(2))  # 3

#-------------------------------------------------------extend()-------------------------------------------------------|
# extend(): Bitta ro'yxatni boshqasiga qo'shish uchun ishlatiladi.
# Qabul qiladigan qiymat: Qo'shiladigan ro'yxat.
# Qaytaradigan qiymat: Yo'q (None).
# Error: Yo'q.
my_list = [1, 2, 3]
other_list = [4, 5, 6]
my_list.extend(other_list)
print(my_list)  # [1, 2, 3, 4, 5, 6]

#-------------------------------------------------------index()--------------------------------------------------------|
# index(): Berilgan elementning indeksini topish uchun ishlatiladi.
# Qabul qiladigan qiymat: Qidiriladigan element.
# Qaytaradigan qiymat: Elementning birinchi indeksi.
# Error: Element topilmadi (ValueError).
my_list = [1, 2, 3, 4, 5]
print(my_list.index(3))  # 2

#-------------------------------------------------------insert()-------------------------------------------------------|
# insert(): Berilgan indeksga yangi elementni qo'shish uchun ishlatiladi.
# Qabul qiladigan qiymatlar: Indeks va qo'shiladigan element.
# Qaytaradigan qiymat: Yo'q (None).
# Error: Indeks to'g'ri kelmadi (IndexError).
my_list = [1, 2, 3]
my_list.insert(1, 4)
print(my_list)  # [1, 4, 2, 3]

#--------------------------------------------------------pop()---------------------------------------------------------|
# pop(): Berilgan indeksga tegishli elementni olib tashlash uchun ishlatiladi.
# Qabul qiladigan qiymat: Indeks (agar ko'rsatilmagan bo'lsa, oxirgi elementni olib tashlaydi).
# Qaytaradigan qiymat: Olib tashlangan element.
# Error: Indeks to'g'ri kelmadi (IndexError).
my_list = [1, 2, 3]
popped_element = my_list.pop(1)
print(popped_element)  # 2

#-------------------------------------------------------remove()-------------------------------------------------------|
# remove(): Berilgan elementni ro'yxatdan o'chirish uchun ishlatiladi.
# Qabul qiladigan qiymat: O'chiriladigan element.
# Qaytaradigan qiymat: Yo'q (None).
# Error: Element topilmadi (ValueError).
my_list = [1, 2, 3]
my_list.remove(2)
print(my_list)  # [1, 3]

#------------------------------------------------------reverse()-------------------------------------------------------|
# reverse(): Ro'yxatni teskari tartibda joylash uchun ishlatiladi.
# Qabul qiladigan qiymat: Yo'q.
# Qaytaradigan qiymat: Yo'q (None).
# Error: Yo'q.
my_list = [1, 2, 3]
my_list.reverse()
print(my_list)  # [3, 2, 1]

#--------------------------------------------------------sort()--------------------------------------------------------|
# sort(): Ro'yxatni o'sish tartibida saralash uchun ishlatiladi.
# Qabul qiladigan qiymatlar: key (saralish funktsiyasi) va reverse (bo'lmaguncha).
# Qaytaradigan qiymat: Yo'q (None).
# # Error: Yo'q.
my_list = [3, 1, 2]
my_list.sort()
print(my_list)  # [1, 2, 3]