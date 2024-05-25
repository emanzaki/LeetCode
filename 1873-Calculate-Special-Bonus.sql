select employee_id , CASE 
    when (name not like 'M%' and employee_id % 2 <> 0) then salary
    else 0 
End as bonus
from Employees order by employee_id