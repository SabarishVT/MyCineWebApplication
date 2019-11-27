create database mycineUserDB;
use mycineUserDB;
CREATE TABLE user_details ( 
id smallint unsigned not null auto_increment, 
user_name varchar(20) not null,
password varchar(256) not null,
age smallint unsigned not null,
gender varchar(30) not null,
email varchar(50) not null,
address varchar(256) not null,
phone long not null,
country varchar(100) not null,
primary key (id) 
);