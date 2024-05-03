CREATE TABLE city (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(17) NOT NULL,
  countrycode VARCHAR(3) NOT NULL,
  population INT NOT NULL
);

INSERT INTO city (name, countrycode, population) VALUES ('Tashkent', 'UZB', 2579000), ('New York City', 'USA', 8538000), ('Moscow', 'RUS', 12615000), ('London', 'GBR', 8974000), ('Beijing', 'CHN', 21516000), ('Tokyo', 'JPN', 37339000), ('Paris', 'FRA', 2165000), ('Berlin', 'DEU', 3769000), ('Istanbul', 'TUR', 15020000), ('Cairo', 'EGY', 9500000);

SELECT
  (SELECT COUNT(*) FROM city WHERE population < 1000000) AS count_less_than_million,
  (SELECT COUNT(*) FROM city WHERE population >= 1000000) AS count_more_than_million
FROM DUAL;


SELECT name, population FROM city WHERE countrycode = 'UZB';
