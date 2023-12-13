-- script that creates the db hbtn_0d_2 and the user user_0d_2
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- create a table state
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(256) NOT NULL
);
