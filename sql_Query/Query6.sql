use mycineuserdb;
CREATE TABLE medicine_details ( 
id smallint unsigned not null , 
disease varchar(100) not null,
tablets varchar(100) not null,
homeremedy varchar(256) not null,
doctor varchar(100) not null
);