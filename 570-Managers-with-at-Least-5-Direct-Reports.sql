# Write your MySQL query statement below
select s.name from Employee e
join Employee s
on e.managerId = s.id
group by e.managerId
having count(e.managerId) >= 5
