--- create / drop databse

CREATE DATABSE <db-name>

DROP DATABSE [IF-EXIST] <db-name>

CREATE DATABASE mydata
WITH
	OWNER tsemach
	ENCODING 'UTF8'
	LC_COLLATE = 'C'
	LC_TYPE = 'C'
	TABLESPACE = pg_default
	CONNECTION LIMIT = -1;
  
