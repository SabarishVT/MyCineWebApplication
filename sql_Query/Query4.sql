DELIMITER $$

USE `mycineuserdb`$$

CREATE PROCEDURE `Add_User`(
	IN p_name VARCHAR(45),
	IN p_password VARCHAR(255),
    IN p_age int,
    IN p_gender VARCHAR(30),
    IN p_email VARCHAR(45),
    IN p_address VARCHAR(255),
    IN p_phone long,
    IN p_country VARCHAR(100)
    
    )
BEGIN
		IF ( SELECT EXISTS (SELECT 1 FROM user_details WHERE user_name = p_name) ) THEN     
			SELECT 'Username Exists !!';		     
		    ELSE		     
			INSERT INTO user_details
			(
			    user_name,
                password,
                age,
                gender,
			    email,
			    address,
                phone,
                country
			)
			VALUES
			(
			    p_name,
                p_password,
                p_age,
                p_gender,
                p_email,
                p_address,
                p_phone,
                p_country
			    
			    
			);
		    END IF;
	END$$

DELIMITER ;