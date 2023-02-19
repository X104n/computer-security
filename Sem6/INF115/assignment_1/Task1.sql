-- Task 1

-- a)
-- Write a query to create the table called Ratings. Pay attention to the
-- restrictions.

DROP TABLE IF EXISTS `Ratings`;
CREATE TABLE `Ratings` (
  `user_id` int(11) NOT NULL,
  `product_id` int(11) NOT NULL,
  `rate` int(1) NOT NULL CHECK ( `rate` >= 0 AND `rate` <= 5),
  `comment` varchar(1000)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- b)
-- Write queries to insert the values from Ratings data.sql

insert into `Ratings` (user_id,product_id,rate,comment) values
(1, 86, 3, 'Could be better, but still functional.'),
(2, 74, 3, 'Could use some improvement.'),
(7, 102, 4, 'Solid product, no major complaints.'),
(8, 60, 4, 'Satisfied with my purchase.'),
(9, 94, 5, 'Excellent product, exceeded expectations!'),
(10, 113, 5, 'Incredible product, would buy again!'),
(11, 68, 5, 'Excellent product, exceeded expectations.'),
(12, 83, 4, 'Good value for the price.'),
(13, 80, 2, 'Disappointed, not as expected.'),
(14, 67, 2, 'Poor quality, would not recommend.'),
(15, 100, 4, 'Solid product, no major complaints.'),
(16, 69, 2, 'Disappointed, not as expected.'),
(17, 99, 5, 'Love this product, would buy again.'),
(18, 65, 3, 'Could be better, but still functional.'),
(19, 80, 4, 'Good product, easy to use.'),
(21, 57, 4, 'Good product, would buy again.'),
(22, 19, 4, 'Good product, would buy again.'),
(23, 60, 3, 'Decent product, nothing special.'),
(24, 53, 3, 'Average product, not sure if I would buy again.'),
(25, 109, 4, 'Good product, would buy again.'),
(26, 92, 4, 'Satisfied with my purchase.'),
(29, 75, 4, 'Good value for the price.'),
(30, 79, 4, 'Good product, would recommend.'),
(31, 108, 5, 'Love this product, would buy again.'),
(32, 104, 5, 'Great product, would buy again.'),
(35, 66, 2, 'Poor quality, would not recommend.'),
(36, 104, 4, 'Good product, would buy again.'),
(40, 45, 3, 'Just okay, not sure if I would buy again.'),
(41, 6, 5, 'Impressive product, highly recommend!'),
(42, 106, 5, 'Amazing product, definitely worth it!'),
(45, 84, 5, 'Amazing product, definitely worth it!'),
(46, 114, 5, 'Impressive product, highly recommend!'),
(47, 89, 4, 'Good product, easy to use.'),
(48, 101, 4, 'Good product for the price.'),
(49, 38, 3, 'Could use some improvement.'),
(50, 112, 5, 'Excellent product, exceeded expectations!');

-- c)
-- Increase the price of tablets in the Products table by 20%

UPDATE products 
SET price = price * 1.2 
WHERE category = 'Tablet';

-- d) 
-- Decreases the number of smartphones in stock by one, and for those that
-- are out of stock, it does not change.

UPDATE products 
SET quantity = quantety - 1 
WHERE category = 'smartphones' 
AND quantity >= 1;

