# Write your MySQL query statement below
select employee_id from Employees
where employee_id not in (select s.employee_id from Salaries as s)
union 
select employee_id from Salaries 
where not employee_id in (select e.employee_id from Employees as e  )
order by employee_id