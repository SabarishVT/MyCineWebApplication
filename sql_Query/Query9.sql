DELIMITER $$

USE `mycineuserdb`$$

CREATE  PROCEDURE `ViewTablets`()
BEGIN
	SELECT * FROM medicine_details;	
END$$

DELIMITER ;