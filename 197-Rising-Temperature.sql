# Write your MySQL query statement below
select e.id from Weather w
join Weather e
on DATE_ADD(w.recordDate, INTERVAL 1 DAY) = e.recordDate 
where e.temperature > w.temperature