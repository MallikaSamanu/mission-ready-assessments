SELECT * FROM jobs_data;

-- Q1:What are all job titles and the corresponding salaries in USD?
select distinct 
job_title, 
salary_in_usd 
from jobs_data
order by job_title,salary_in_usd;

-- Q2:What are jobs that are categorized under 'Data Scientist' or 'Data Analyst' and display their work year and salary.
select distinct
job_title, 
job_category, 
work_year,
salary
from jobs_data
where job_title = 'Data Scientist' or job_title = 'Data Analyst'
order by 1,2,3,4;

-- Q3:What are all jobs where the salary in USD is above $100,000, including their job titles, salaries in USD, and company locations?
select distinct
experience_level,
employment_type,
job_title
from jobs_data
where experience_level= 'Senior'
and employment_type= 'Full-time'
order by 1,2,3;

-- Q4:What are all jobs where the salary in USD is above $100,000, including their job titles, salaries in USD, and company locations?

select 
job_title,
salary_in_usd,
company_location
from jobs_data
where salary_in_usd > 100000;

-- Q5:What are jobs located in 'US' with a work setting of 'Remote', along with their job titles, company sizes, and salaries in USD?
select 
company_location,
work_setting,
job_title,
company_size,
salary_in_usd
from jobs_data
where company_location='United States' 
and work_setting='Remote';

-- Q6:For all employees with a senior experience level ('Senior') and a company size of 'Large', find their job titles, company locations, and salaries?

select
experience_level,
company_location,
job_title,
company_size,
salary
from jobs_data
where experience_level='Senior' 
and company_size='L';

-- Q7:Can you list the average salary in USD for each job title?

select 
job_title,
avg(salary_in_usd)
from jobs_data
group by job_title
order by job_title;

-- Q8:Find any employees with incorrect employment type marked as 'PT' (part-time) but whose salary indicates they are full-time (salary above $50,000), and update their employment types to 'FT'.

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

-- Q9:What are records where the job title is missing or listed as 'Unknown', and update these records with the job title 'Data Specialist'?
select *
from jobs_data
where job_title ='Unknown' or job_title = '';
SET SQL_SAFE_UPDATES = 0;
update jobs_data
set job_title ='Data Specialist'
where job_title ='Unknown' or job_title = '';

-- Q10:What is the action to delete all records from the job_listings table where the salary is below $70,000?
/*
delete from
jobs_data
where salary<70000;
*/
