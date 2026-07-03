create database movie_practice;
use movie_practice;
drop table actors;

create table actors (
id int auto_increment primary key , 
name text not null, 
birth_year int not null , 
nationality text not null
);

insert into actors (name,birth_year,nationality)
 values( 'Leonardo DiCaprio', 1974, 'American'),
('Meryl Streep',1949,'American'),
('Denzel Washington',1954,'American');

insert into actors (name,birth_year)
 values( 'Leonardo DiCaprio', 1974);
 
select * from actors;


