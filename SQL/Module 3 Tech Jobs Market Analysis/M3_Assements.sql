SELECT * FROM jobs_data;

-- Q1
select distinct 
job_title, 
salary_in_usd 
from jobs_data
order by job_title,salary_in_usd;

-- Q2
select distinct
job_title, 
job_category, 
work_year,
salary
from jobs_data
where job_title = 'Data Scientist' or job_title = 'Data Analyst'
order by 1,2,3,4;

-- Q3
select distinct
experience_level,
employment_type,
job_title
from jobs_data
where experience_level= 'Senior'
and employment_type= 'Full-time'
order by 1,2,3;

-- Q4

select 
job_title,
salary_in_usd,
company_location
from jobs_data
where salary_in_usd > 100000;

-- Q5
select 
company_location,
work_setting,
job_title,
company_size,
salary_in_usd
from jobs_data
where company_location='United States' 
and work_setting='Remote';

-- Q6

select
experience_level,
company_location,
job_title,
company_size,
salary
from jobs_data
where experience_level='Senior' 
and company_size='L';

-- Q7

select 
job_title,
avg(salary_in_usd)
from jobs_data
group by job_title
order by job_title;

-- Q8

select 
employment_type,
salary
from jobs_data
where salary > 50000 and employment_type='Part-time';

SET SQL_SAFE_UPDATES = 0;
update jobs_data
set employment_type='Full-time'
where salary > 50000 and employment_type='Part-time';
SET SQL_SAFE_UPDATES = 1;

-- Q9
select *
from jobs_data
where job_title ='Unknown' or job_title = '';
SET SQL_SAFE_UPDATES = 0;
update jobs_data
set job_title ='Data Specialist'
where job_title ='Unknown' or job_title = '';

-- Q10
/*
delete from
jobs_data
where salary<70000;
*/
