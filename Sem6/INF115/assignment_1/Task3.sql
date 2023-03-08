-- Task 3

-- a)
-- Write a query to show all products with a rating strictly greater than 2.

select p.* , avg(r.rate) as average_rate
from ratings as r
join products as p
on r.product_id = p.product_id
group by r.product_id
having average_rate > 2
order by average_rate desc;

-- b)
-- Write a query to show all products sold on 2010-02-03

select p.*, o.registered_date
from orders as o
join ordersproducts as op
on o.order_id = op.order_id
join products as p
on op.product_id = p.product_id
where registered_date = '2010-02-03';

-- c)
-- Write a query to show all users who placed orders more than two times

select u.*, count(*) as num_orders
from orders as o
join users as u
on o.user_id = u.user_id
group by u.user_id
having count(*) > 2;

-- d)
-- Write a query to display all products where there is an order containing
-- exactly two units of the product for each of the products.

select p.* , op.order_id , op.quantity as order_quantity
from ordersproducts as op
join products as p
on op.product_id = p.product_id
where op.quantity = 2;

-- e)
-- Write a query to show all orders placed by a user with username justin81.

select o.*, u.*
from orders as o
join users as u
on o.user_id = u.user_id
where u.username = 'justin81';
