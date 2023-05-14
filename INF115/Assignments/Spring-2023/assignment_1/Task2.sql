-- Task 2

-- a)
-- Write a query to show all registered users between ’2010-03-02’ and 
-- ’2020-03-02’.

select *
from users
where registered_date
between '2010-03-02' and '2020-03-02'
order by registered_date;

-- b)
-- Write a query to show all products in ascending price order

select *
from products
order by price asc;

-- c)
-- Write a query to show all out-of-stock products.

select *
from products
where quantity = 0;

-- d)
-- Write a query to show the total price for each order id.

select *,
(price * quantity) as total 
from ordersproducts 
group by order_id;

-- e)
-- Write a query to show the average price of in-stock smartphones.

select avg(price) as average_price
from products
where category = 'smartphone' and quantity > 0;
