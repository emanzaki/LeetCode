# Write your MySQL query statement below
select e.name , ei.unique_id from Employees as e
left join EmployeeUNI as ei 
on e.id = ei.id