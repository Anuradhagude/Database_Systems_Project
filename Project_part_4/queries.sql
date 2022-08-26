select * from payment;

select * from product;

Insert Into cart (date, totalprice) values('8/28/22', '200');

select * from cart;

Update cart set totalprice = 145 where date = '8/28/22';

select * from cart where totalprice = 145;

delete from cart where totalprice = 120;

select * from cart;

select * from cart order by totalprice asc;

select * from cart order by totalprice desc;

select * from cart order by date desc;

select * from customer;

select * from customer where Password = 2345;

select pr.description, pr.name, pa.dateTime, pa.amount from product as pr join Payment as pa on pr.custID = pa.custID;

select min(price) from product;

select max(price) from product;

select avg(price) from product;

select count(price) from product;

select pr.description, pr.name, pa.dateTime, pa.amount from product as pr join Payment as pa on pr.custID = pa.custID;
