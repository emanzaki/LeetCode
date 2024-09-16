# Write your MySQL query statement below
select q.query_name , ifnull(round(sum(q.rating/q.position) /count(q.query_name),2) ,0) as quality  , 
ifnull(round(100 * (count(u.rating) /count(q.rating)), 2),0) as poor_query_percentage 
from Queries q
left join Queries u
on u.result = q.result and q.query_name = u.query_name and u.rating < 3  
group by q.query_name 
having q.query_name is not null