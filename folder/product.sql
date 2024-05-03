-- databza mavjud bulmasa yaratish
CREATE DATABASE IF NOT EXISTS product;

-- 2. databazadan foydalanish
USE product;

-- 3. product nomli table yaratish agar mavjud bulmasa.
CREATE TABLE product (
  id INT AUTO_INCREMENT PRIMARY KEY ,
  maker VARCHAR(50) NOT NULL,
  model INT NOT NULL,
  type VARCHAR(50) NOT NULL
);

-- 4. product tablesiga ma'lumot qushish.
INSERT INTO product (maker, model, type)
VALUES ('HP', 12318, 'Kompyuter'),
       ('Acer', 1010, 'Noutbuk'),
       ('Asus', 1378, 'Noutbuk'),
       ('Lenovo', 6711, 'Kompyuter'),
       ('HP', 182193, 'Printer'),
       ('Canon', 6789, 'Printer'),
       ('HP', 1478963, 'Printer'),
       ('LG', 125478, 'Kompyuter'),
       ('Lenovo', 362145, 'Noutbuk'),
       ('Xiaomi', 98763, 'Noutbuk');


 /* 1-vazifa product jadvalidan foydalanib, ihlab chigaruvchi mahsuloti
 fagat bitta type ishlatadigan ma ‘lumotni chiqarish */
SELECT maker
FROM product
GROUP BY maker HAVING COUNT(type)=1;

/* 2-vazifa product jadvalidan foydalanib.
model raqami unikal raqamiardan tashkil topgan mahsulotlarni
type ustuni bo'yicha alifbo tartibida saralab chiqish.*/

-- ushbu shartni sql orqliy yicha olmadim yichinmni python orqaliy qildim 1-task.py faylida

