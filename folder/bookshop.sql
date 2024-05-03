CREATE TABLE `bookshop` (
  `lid` int NOT NULL,
  `name` varchar(50) NOT NULL,
  `author` varchar(50) NOT NULL,
  `year_publish` int NOT NULL,
  `price` double NOT NULL,
  `sale` int NOT NULL,
  `genre` varchar(50) NOT NULL,
  `len_page` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


INSERT INTO `bookshop` (`lid`, `name`, `author`, `year_publish`, `price`, `sale`, `genre`, `len_page`) VALUES
(1, 'Vincent & Theo', 'Raymund Slayny', 2000, 500, 10, 'Western', 500),
(2, 'Charlie Chan\'s Courage', 'Nessy Gibby', 2001, 600, 15, 'Animation', 600),
(3, 'Pin...', 'Sheilah Halliwell', 2002, 700, 5, 'Drama', 700),
(4, 'Same Old Song (On connant la chanson)', 'Cully Boc', 2003, 800, 25, 'Thriller', 800),
(5, 'Santa Claus', 'Leslie Hasling', 2004, 900, 10, 'Drama', 900),
(6, 'Action in the North Atlantic', 'Natassia Turford', 2005, 1000, 15, 'Drama', 1000),
(7, 'Heist', 'Rick Andrews', 2006, 1100, 5, 'Documentary', 1100),
(8, 'Schizopolis', 'Sibilla Stolte', 2007, 1200, 25, 'Drama', 1200),
(9, 'Game of Chance (Onnenpeli)', 'Aldin McConnal', 2008, 1300, 10, 'Thriller', 1300),
(10, 'Anne Frank Remembered', 'Agnese Sporrij', 2009, 1400, 15, 'Western', 1400);


SELECT *
FROM `bookshop``
WHERE `year_publish`` <= 2014
ORDER BY `price`` DESC, `len_page` DESC, `sale` DESC;

SELECT `genre`, COUNT(*) AS `num_books`
FROM `bookshop`
GROUP BY `genre`
ORDER BY `num_books` DESC;