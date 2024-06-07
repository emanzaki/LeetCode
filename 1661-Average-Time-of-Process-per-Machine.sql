# Write your MySQL query statement below
select a.machine_id , round(avg(c.timestamp - a.timestamp), 3) as processing_time from Activity a 
join Activity c 
on (a.machine_id = c.machine_id) and (a.process_id = c.process_id)
where a.activity_type = 'start' and c.activity_type = 'end'
group by a.machine_id