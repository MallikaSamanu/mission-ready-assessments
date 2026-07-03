/* select * from games_description;games_revenue
select genre from games_description
where genre = 'Strategy.';
update games_description
set genre = 'Strategy'
select genre from games_description
where genre = 'Strategy';
SET SQL_SAFE_UPDATES = 1;
*/

-- total revenue

-- Q1
select game_id,
sum(Number_of_Purchases * Unit_Price) as total_revenue from games_revenue
group by game_id;

-- Q2 
select game_id,
sum(Number_of_Purchases * Unit_Price) as total_revenue from games_revenue
group by game_id
order by total_revenue desc
limit 5;

-- Q3

select 
d.genre,
sum(Number_of_Purchases * Unit_Price) as total_revenue
from games_revenue gr
join games_description d
on d.game_id =gr.game_id
group by d.genre
ORDER BY total_revenue DESC;
-- LIMIT 3

-- q4 

select
year_released,
sum(Number_of_Purchases * Unit_Price) as total_revenue
from games_revenue gr
join games_description d
on d.game_id =gr.game_id
group by year_released
ORDER BY total_revenue DESC
LIMIT 1;



-- Review percentage

-- Q5

/* 
select 
reviews.game_id,
reviews.number_of_reviews_from_purchased_people,
revenue.Number_of_Purchases,
(reviews.number_of_reviews_from_purchased_people/revenue.Number_of_Purchases)*100 as review_percentage
from games_reviews reviews
 join games_revenue revenue
on reviews.game_id =revenue.game_id
;
 */

select 
(sum(reviews.number_of_reviews_from_purchased_people)/sum(revenue.Number_of_Purchases))*100 as review_percentage
from games_reviews reviews
 join games_revenue revenue
on reviews.game_id =revenue.game_id
;


-- English Review Analysis

-- Q6

select 
reviews.game_name,
(reviews.number_of_english_reviews/revenue.Number_of_Purchases)*100 as english_review_percentage
from games_reviews reviews
 join games_revenue revenue
on reviews.game_id =revenue.game_id
order by 1
;


 -- Publisher Insights

-- Q7

select gd.publisher,
sum(Number_of_Purchases * Unit_Price) as total_revenue 
from games_revenue gr
join games_description gd
on gd.game_id =gr.game_id
group by gd.publisher
ORDER BY total_revenue DESC
LIMIT 5;


--  Engagement Ratios

-- Q8

-- Calculate the percentage of Helpful and Funny tags to total reviews.
SELECT 
(SUM(gr.Helpful)  / SUM(gr.number_of_reviews_from_purchased_people))*100 AS helpful_pct,
(SUM(gr.Funny)  / SUM(gr.number_of_reviews_from_purchased_people))*100 AS funny_pct
FROM games_reviews gr
;

-- Which games and genres have the highest and lowest percentages?
/*

--game wise
SELECT 
  game_name,
  SUM(Helpful) * 100.0 / NULLIF(SUM(number_of_reviews_from_purchased_people), 0) AS highest_helpful_pct
FROM games_reviews
GROUP BY game_name
ORDER BY 2 DESC
LIMIT 1;

SELECT 
  game_name,
  SUM(Helpful) * 100.0 / NULLIF(SUM(number_of_reviews_from_purchased_people), 0) AS lowest_helpful_pct
FROM games_reviews
GROUP BY game_name
ORDER BY 2 
LIMIT 1;

SELECT 
  game_name,
  SUM(Funny) * 100.0 / NULLIF(SUM(number_of_reviews_from_purchased_people), 0) AS highest_funny_pct
FROM games_reviews
GROUP BY game_name
ORDER BY 2 DESC
LIMIT 1;

SELECT 
  game_name,
  SUM(Funny) * 100.0 / NULLIF(SUM(number_of_reviews_from_purchased_people), 0) AS lowest_funny_pct
FROM games_reviews
GROUP BY game_name
ORDER BY 2 
LIMIT 1;

--genre wise

SELECT 
  d.genre,
  SUM(gr.Helpful) * 100.0 / NULLIF(SUM(gr.number_of_reviews_from_purchased_people), 0) AS highest_helpful_pct
FROM games_reviews gr
JOIN games_description d
  ON gr.game_id = d.game_id
GROUP BY d.genre
ORDER BY 2 DESC
LIMIT 1;


SELECT 
  d.genre,
  SUM(gr.Helpful) * 100.0 / NULLIF(SUM(gr.number_of_reviews_from_purchased_people), 0) AS lowest_helpful_pct
FROM games_reviews gr
JOIN games_description d
  ON gr.game_id = d.game_id
GROUP BY d.genre
ORDER BY 2 ASC
LIMIT 1;

SELECT 
  d.genre,
  SUM(gr.Funny) * 100.0 / NULLIF(SUM(gr.number_of_reviews_from_purchased_people), 0) AS hghest_funny_pct
FROM games_reviews gr
JOIN games_description d
  ON gr.game_id = d.game_id
GROUP BY d.genre
ORDER BY 2 DESC
LIMIT 1;

SELECT 
  d.genre,
  SUM(gr.Funny) * 100.0 / NULLIF(SUM(gr.number_of_reviews_from_purchased_people), 0) AS lowest_hghest_funny_pct
FROM games_reviews gr
JOIN games_description d
  ON gr.game_id = d.game_id
GROUP BY d.genre
ORDER BY 2 
LIMIT 1;

*/

select * from games_reviews
where game_name in ('Terrari','The Ram');

WITH game_stats AS (
  SELECT 
    gr.game_name AS name,
    'Game' AS type,
    SUM(gr.Helpful) * 100.0 / NULLIF(SUM(gr.number_of_reviews_from_purchased_people), 0) AS helpful_pct,
    SUM(gr.Funny) * 100.0 / NULLIF(SUM(gr.number_of_reviews_from_purchased_people), 0) AS funny_pct
  FROM games_reviews gr
  GROUP BY gr.game_name
),

genre_stats AS (
  SELECT 
    d.genre AS name,
    'Genre' AS type,
    SUM(gr.Helpful) * 100.0 / NULLIF(SUM(gr.number_of_reviews_from_purchased_people), 0) AS helpful_pct,
    SUM(gr.Funny) * 100.0 / NULLIF(SUM(gr.number_of_reviews_from_purchased_people), 0) AS funny_pct
  FROM games_reviews gr
  JOIN games_description d
    ON gr.game_id = d.game_id
  GROUP BY d.genre
),

all_stats AS (
  SELECT * FROM game_stats
  UNION ALL
  SELECT * FROM genre_stats
)

 -- select * from all_stats;
,

ranked AS (
  SELECT *,
    RANK() OVER (PARTITION BY type ORDER BY helpful_pct DESC) AS max_helpful,
    RANK() OVER (PARTITION BY type ORDER BY helpful_pct ASC) AS min_helpful,
    RANK() OVER (PARTITION BY type ORDER BY funny_pct DESC) AS max_funny,
    RANK() OVER (PARTITION BY type ORDER BY funny_pct ASC) AS min_funny
  FROM all_stats
)
-- select * from ranked;
SELECT 
  type,
  name,
  helpful_pct,
  funny_pct,
  CASE 
    WHEN max_helpful = 1 THEN 'Highest Helpful'
    WHEN min_helpful = 1 THEN 'Lowest Helpful'
    WHEN max_funny = 1 THEN 'Highest Funny'
    WHEN min_funny = 1 THEN 'Lowest Funny'
  END AS category
FROM ranked

;
   
   
   -- Task 4.  Advanced SQL: Window Functions
WITH game_metrics AS (
SELECT 
gr.game_id,grv.game_name,
-- Total Revenue
SUM(gr.Number_of_Purchases * gr.Unit_Price) AS total_revenue,
-- Total Reviews
SUM(grv.number_of_reviews_from_purchased_people) AS total_reviews
FROM games_revenue gr
JOIN games_reviews grv
ON gr.game_id = grv.game_id
GROUP BY gr.game_id,grv.game_name
)
SELECT 
game_id,game_name,
total_revenue,
total_reviews,
-- Rank by Revenue within Genre
RANK() OVER (ORDER BY total_revenue DESC) AS revenue_rank,
-- Rank by Reviews within Genre
RANK() OVER ( ORDER BY total_reviews DESC) AS review_rank
FROM game_metrics
;

-- Use RANK() to rank games by their total revenue within each genre.
-- Use RANK() to rank games by their total reviews within each genre.


select genre,count(*) from games_description
group by genre;


WITH genre_metrics AS (
SELECT 
gd.genre,count(*) as game_count,
-- Total Revenue
SUM(gr.Number_of_Purchases * gr.Unit_Price) AS total_revenue,
-- Total Reviews
SUM(grv.number_of_reviews_from_purchased_people) AS total_reviews
FROM games_revenue gr
JOIN games_reviews grv ON gr.game_id = grv.game_id
JOIN games_description gd ON gr.game_id = gd.game_id
GROUP BY gd.genre
)
SELECT 
genre,game_count,
total_revenue,
total_reviews,
-- Rank by Revenue within Genre
RANK() OVER (ORDER BY total_revenue DESC) AS revenue_rank,
-- Rank by Reviews within Genre
RANK() OVER ( ORDER BY total_reviews DESC) AS review_rank
FROM genre_metrics
;






SELECT game_name, genre, publisher, number_of_Purchases * Unit_Price AS 'Revenue',
RANK () OVER (PARTITION BY games_description.genre ORDER BY (number_of_Purchases * Unit_Price) DESC) AS 'Rank'
FROM games_revenue
INNER JOIN games_description
ON games_revenue.game_id = games_description.game_id;
 
 
-- RANK by reviews in each genre
SELECT* 
FROM games_reviews;
 
SELECT games_description.game_name, genre, publisher, number_of_reviews_from_purchased_people,
RANK () OVER (PARTITION BY games_description.genre ORDER BY number_of_reviews_from_purchased_people DESC) AS 'Rank'
FROM games_reviews
INNER JOIN games_description
ON games_reviews.game_id = games_description.game_id;
