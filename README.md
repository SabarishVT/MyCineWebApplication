# MyCineWebApplication
Flask based web framework which provides suggestions to patients based on disease symptoms

### README File for MYCINE Web application Project

> Prerequisites:

+ __MYSQL (root or any user)__
+ __Python Flask webframework__

`Steps to follow before project initiation`

1. Create a database named mycineUserDB in mysql by passing the following query

```MySQL
use mycineUserDB;
```

2. Create a table named user_details with column indexes as follows:

```MySQL
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
phone integer not null,
country varchar(100) not null,
primary key (id)
);
```

3. Create a View_User_Details query for listing the user details from MySQL

```MySQL
DELIMITER $$

USE `mycineuserdb`$$

CREATE  PROCEDURE `View_User_Details`()
BEGIN
	SELECT * FROM user_details;
END$$

DELIMITER ;
```
__To call the stored user in mysql just use call View_User_Details();__

4. Create a stored procedure named Add_User for adding the user details from the register webpage into the database

```MySQL


```
__To call the stored procedure CALL Add_User('Sabarish','sabarish4fun@gmail.com','sabru',28,'male','Bangalore','8220694738','India');__

5. Create the second table in our database to store the medicine user_details

```MySQL
use mycineuserdb;
CREATE TABLE medicine_details (
id smallint unsigned not null ,
disease varchar(100) not null,
tablets varchar(100) not null,
homeremedy varchar(256) not null,
doctor varchar(100) not null
);
```

6. Create a stored procedure to add details in the medicine details table

```MySQL
DELIMITER $$

USE `mycineuserdb`$$

CREATE PROCEDURE `Add_tablets`(
	IN t_id int,
    In t_disease varchar(100),
	IN t_tablets VARCHAR(100),
	IN t_homeremedy VARCHAR(256),
	IN t_doctor VARCHAR(100)
    )
BEGIN
		IF ( SELECT EXISTS (SELECT 1 FROM medicine_details WHERE id = t_id) ) THEN     
			SELECT 'Symptom already Exists !!';		     
		    ELSE		     
			INSERT INTO medicine_details
			(
			    id,
			    disease,
                tablets,
                homeremedy,
                doctor
			)
			VALUES
			(
			    t_id,
			    t_disease,
			    t_tablets,
                t_homeremedy,
                t_doctor
			);
		    END IF;
	END$$

DELIMITER ;
```

7. Create a query for stored procedure callproc

```MySQL
#call Add_tablets(1,'Influenza(flu)adults ','Rapivals,Relenza,Tamiflu','Tea,Lemon,Honey','Dr.S.V.Jain');
#call Add_tablets(2,'Appendicities','Zosyn,Invanz,Maxipime','Fenugreek seeds,Cucumber,Beet root','Dr.Veeresh');
#call Add_tablets(3,'Common cold','dcold,advil,tylenol','papaya,bran,milk','Dr.Kavitha');
#call Add_tablets(4,'Common cold','dcold,advil,tylenol','ginger,honey','Dr.Hanumesh shetty');
#call Add_tablets(5,'Viral pneumonia','Tamiflue,Relenza,Rapivals','drink plenty of fluids','Dr.Preeti');
#call Add_tablets(6,'Irritable bowel','Eluxadoline,Rifaximin,Linaclotide','Yogurt,Psyllium husks,Isabgol','Dr.Sana');
#call Add_tablets(7,'Appendicities','Zosyn,Invanz,Maxipime','Fenugreek seeds,Cucumber,Beet root','Dr.Khaja moinuddin');
#call Add_tablets(8,'Acute Sinusities','Sudafed,Tylenol','Fenugreek seeds,water','Dr.Rahguveer')
#call Add_tablets(9,'Intestinal Obsturction','Phenergan,Phenadoz,Promethegam','Lemon tea,Honey,water','Dr.Susheela')
#call Add_tablets(10,'Gas','Rentidine,Eno,Zintac','Lemon juice,Fennel seeds','Dr.Balaji')
#call Add_tablets(11,'Cough','Mucine,vicks','Mint and Tulsi leaves','Dr.Mansoor ali')
#call Add_tablets(12,'Migrane headache','Naproxin,Acetaminopheb,Ibuprofen','Amaranthus polygonoids,black pepper,ginglly oil and turmeric','Dr.Indira')
#call Add_tablets(13,'Acute Sinusities','Sudafed,Tylenol','Fenugreek seeds,water','Dr.venkat')
#call Add_tablets(14,'Drug allergy','Antihistamine,Benadryl','Turmeric,Dry gourd,Black pepper,Fodder','Dr.Adarsha')
#call Add_tablets(15,'Irritable bowel','Eluxadoline,Rifaximin,Linaclotide','Yogurt,Psyllium husks,Isabgol','Dr.Adna')
#call Add_tablets(16,'Heat cramps','Cystelia M,Follicells,Feminine','Raggi malt,drink more water,yogurt','Dr.Mohammed Farooqh Javvad Ali')
#call Add_tablets(17,'Drug allergy','Antihistamine,Benadryl','Turmeric,Dry gourd,Black pepper,Fodder','Dr.Ajay')
#call Add_tablets(18,'Drug allergy','Antihistamine,Benadryl','Turmeric,Dry gourd,Black pepper,Fodder','Dr.Sanjay')
call Add_tablets(19,'Drug allergy','Antihistamine,Benadryl','Turmeric,Dry gourd,Black pepper,Fodder','Dr.Aruna')
```

8. Create another trigger procedure to list the details of medicine table

```MySQL
DELIMITER $$

USE `mycineuserdb`$$

CREATE  PROCEDURE `ViewTablets`()
BEGIN
	SELECT * FROM medicine_details;
END$$

DELIMITER ;
```
__To list the details call ViewTablets();__


## Project Steps:

> #### Optional If You are using anaconda

` cd toWorkingDirectory`

` conda create -n MYCINE python=3.7`

` conda activate MYCINE`

> Library's to Install:

__flask==1.1.1__

__flask-mysqldb==0.2.0__

##### for installing the requirement library, run the following commands in command prompt

`pip install -r requiremnts.txt`

## Run python app.py
