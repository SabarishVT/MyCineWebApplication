DELIMITER $$

USE `mycineuserdb`$$

CREATE  PROCEDURE `View_User_Details`()
BEGIN
	SELECT * FROM user_details;	
END$$

DELIMITER ;