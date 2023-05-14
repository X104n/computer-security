-- Task 4

-- a)
-- Write a query to show all products that have not been rated.

select *
from products
where product_id
not in(
select product_id 
from ratings)
order by product_id;

-- b)
-- Write a query to display all products with price changes since the product’s
-- last order

select p.*, op.price
from products as p
join ordersproducts as op
on p.product_id = op.product_id
join orders as o
on o.order_id = op.order_id
where p.price != op.price and o.registered_date =
(select max(o.registered_date)
from orders as o
join ordersproducts as op
on o.order_id = op.order_id
where op.product_id = p.product_id)
;
-- c)
-- Write a query to show the most favorite products, i.e., products with the
-- highest ratings.

select p.*, avg(r.rate) as average_rate
from ratings as r
join products as p
on r.product_id = p.product_id
group by r.product_id
having average_rate = 
(select max(sub.average_rate) 
from 
(select avg(rate) as average_rate 
from ratings
group by product_id) sub)
order by average_rate desc;

-- d)
-- Write a query to determine the average daily sales of each product from
-- ”2005-04-08” to ”2023-02-24”. (Hint: first, find out how many of each
-- product have been sold from ”2010-04-08” to ”2023-02-24”, then calculate
-- the average. Functions DATEDIFF(date1,date2) calculates the number of
-- days between two dates.)

select p.*, 
SUM(op.quantity) / datediff('2023-02-24','2005-04-08') as price
from orders as o
join ordersproducts as op
on o.order_id = op.order_id
join products as p
on op.product_id = p.product_id
where o.registered_date between '2005-04-08' and '2023-02-24'
group by op.product_id
order by price desc;
