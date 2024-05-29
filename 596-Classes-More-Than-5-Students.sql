# Write your MySQL query statement below
SELECT c.class
FROM Courses AS c
GROUP BY c.class
having count(c.student) >= 5;
