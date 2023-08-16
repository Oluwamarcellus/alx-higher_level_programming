-- creating and granting new user all permissions to the server
CREATE USER
    IF NOT EXISTS 'user_0d_1'@'localhost'
    IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES 
    ON *.* 
    TO 'user_0d_1'@'localhost';
