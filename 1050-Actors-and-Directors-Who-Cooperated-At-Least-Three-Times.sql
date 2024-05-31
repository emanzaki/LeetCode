# Write your MySQL query statement below
select c.actor_id , c.director_id
from ActorDirector as c
group by c.actor_id , c.director_id
having count(c.timestamp) >= 3
