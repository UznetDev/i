
-- fruit jadvalini yaratish
CREATE TABLE IF NOT EXISTS fruit (
  id INT NOT NULL AUTO_INCREMENT,
  fruit_name VARCHAR(255) NOT NULL,
  fruit_price INT NOT NULL,
  fruit_type VARCHAR(255) NOT NULL,
  PRIMARY KEY (id)
);

-- Fruit jadvaliga ma'lumot qushish
INSERT INTO fruit (fruit_name, fruit_price, fruit_type)
VALUES ('Olma', 12000, 'Golden'),
       ('Gilos', 15000, 'Chereshnya'),
       ('Anor', 20000, 'Qizilorda'),
       ('Uzum', 25000, 'Husayn Tukli'),
       ('Shaftoli', 30000, 'None'),
       ('Olma', 12000, 'Golden'),
       ('Gilos', 15000, 'Chereshnya'),
       ('Anor', 20000, 'Qizilorda'),
       ('Uzum', 25000, 'Husayn'),
       ('Shaftoli', 30000, 'Tukli');


-- 1-task) Fruit jadvalidagi barcha datasi birxil bulgan row larni uchirish
DELETE f2 FROM fruit as f1
INNER JOIN fruit as f2 ON f1.fruit_name = f2.fruit_name AND
 f1.fruit_price=f2.fruit_price AND
  f1.fruit_type=f2.fruit_type AND f1.id < f2.id;

-- fruit jadvalidagi nomi bir xel bulgan datalarni uchirish
DELETE f2 FROM fruit as f1
INNER JOIN fruit as f2 ON f1.fruit_name = f2.fruit_name AND f1.id < f2.id;

-- 2-task) Fruit jadvalidagi engqimmat 3 ta mevani chiqarish
SELECT *
FROM fruit
ORDER BY fruit_price DESC
LIMIT 3;