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