# Write your MySQL query statement below
select * , 
    Case
        When (z < y + x) and (x < y+z) and (y < z +x) then 'Yes'
        else 'No'
    end
    as triangle
from Triangle