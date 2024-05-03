/* table yaratish */
CREATE TABLE participant (
  id INT PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  surname VARCHAR(255) NOT NULL,
  age INT,
  address TEXT
);

/* Ma'lumot qushish */
INSERT INTO participant (id, name, surname, age, address)
VALUES (1, 'Abdulla', 'Abdullayev', 25, 'Toshkent sh., M.Ulug\'bek tumani, Bobur ko\'chasi 5-uy'),
       (2, 'Nodira', 'Abdullayeva', 22, 'Toshkent sh., M.Ulug\'bek tumani, Bobur ko\'chasi 5-uy'),
       (3, 'Shoxrux', 'Rustamov', 20, 'Toshkent sh., Chilonzor tumani, Namatak ko\'chasi 1-uy 25-honadon'),
       (4, 'Hilola', 'Rasulova', 21, 'Toshkent sh., Chilonzor tumani, Jalilov ko\'chasi 5-uy 2-honadon'),
       (5, 'Jalil', 'Rasulov', 18, 'Toshkent sh., Chilonzor tumani, Jalilov ko\'chasi 5-uy 2-honadon'),
       (6, 'Temur', 'Qodirov', 23, 'Toshkent sh., Yashnobod tumani, Safiya ko\'chasi, 25-uy'),
       (7, 'Sardor', 'Kamolov', 20, 'Toshkent sh., Yunusobod tumani, 2-kvartal, 4-uy 75-honadon'),
       (8, 'Botir', 'Malikov', 19, 'Toshkent sh., Mirobod tumani, Temuriylar ko\'chasi, 12-uy'),
       (9, 'Lola', 'Kamolova', 24, 'Toshkent sh., Yunusobod tumani, 2-kvartal, 4-uy 75-honadon'),
       (10, 'Maftuna', 'Farruxova', 19, 'Toshkent sh., Olmazor tumani, Amir Temur ko\'chasi, 4-uy 63-honadon');

SELECT * FROM `participant` WHERE surname like '%' || @surname || '%';


/* 1-vazifa: User jadvalidan foydalanib, oilali foydalanuvchilar haqida ma’lumotlarni chiqarish. */
SELECT
FROM participant AS p1
INNER JOIN participant AS p2
ON p2.surname LIKE CONCAT(p1.surname, '%a') AND p1.address=p2.address;


/* 2-vazifa: User jadvalidan foydalanib, oila qurmagan foydalanuvchilar haqida ma’lumotlarni chiqarish. */
SELECT * FROM participant WHERE address in (
    SELECT address
    FROM participant AS p
    GROUP BY address
    HAVING COUNT(address)=1
);