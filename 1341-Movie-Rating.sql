
(select name as results from Users as u
join MovieRating as mr
on u.user_id = mr.user_id
group by u.name
order by count(mr.user_id) desc , u.name asc 
limit 1)
union all
(select title as results from Movies as m
join MovieRating as mrr
on m.movie_id = mrr.movie_id
where  mrr.created_at like '2020-02-%'
group by m.title
order by avg(mrr.rating) desc , m.title asc
limit 1)

