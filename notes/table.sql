-- create a table 
CREATE TABLE actors (
	actor_id SERIAL PRIMARY KEY,
	first_name VARCHAR(150),
	last_name VARCHAR(150) NOT NULL,
	gender CHAR(1),
	date_of_dirth DATE,
	add_date DATE,
	update_date DATE	
);

-- create table movie with foreign key.
-- read a record with take the director record from directors table a add it to the result of movie
CREATE TABLE movies (
	movie_id SERIAL PRIMARY KEY,
	movie_name VARCHAR(100) NOT NULL,
	movie_length INT,
	movie_lang VARCHAR(20),
	age_certificate VARCHAR(10),
	release_date DATE,
	director_id INT REFERENCES directors (director_id)
);


-- NUMERIC(10,2) - is 10 digits number with two places after the decimal point.
CREATE TABLE movies_revenues (
	revenue_id SERIAL PRIMARY KEY,
	movie_id INT REFERENCES movies (movie_id),
	revenues_domestic NUMERIC (10,2),
	revenues_intenational NUMERIC (10,2)
);

-- junction table, a connection between two tables
-- primary key is a combinatio of two existing keys
CREATE TABLE movies_actors (	
	movie_id INT REFERENCES movies (movie_id),
	actor_id INT REFERENCES actors (actor_id),
	PRIMARY KEY(movie_id, actor_id)
);

CREATE TABLE t_tags (
  id SERIAL PRIMARY KEY,
  tag text UNIQUE,
  update_date TIMESTAMP DEFAULT now()
);

ALTER TABLE persons 
ALTER COLUMN age TYPE int 
USING age::integer;

-- change column to have default value
----------------------------------------------------
ALTER TABLE persons
ADD COLUMN is_enable VARCHAR(1);

ALTER TABLE persons
ADD COLUMN is_enable SET DEFAULT 'Y';
----------------------------------------------------

-- adding constrain to an existing column
ALTER TABLE my_table
ADD CONSTRAINT unique_web_url UNIQUE (my_web_url_column);

-- check in insert / modify that column is_enable include only 'Y' or 'N'
ALTER TABLE web_links
ADD CHECK (is_enable IN ('Y', 'N'));

-- create user defined types
CREATE DOMAIN positive_number INT NOT NUL CHECK (VALUE > 0)
CREATE TABLE sample (
  id SERIAL PRIMARY KEY,
  age positive_number
)

-- create postal code domain
CREATE DOMAIN us_postal_code AS TEXT 
CHECK (
  VALUE ~'\d{5}$',
  OR VALUE ~'^\D{5}-\d{4}$'
)

-- create new composite data type
CREATE TYPE address AS (
  city VARCHAR(20),
  country VARCHAR(20
)
INSERT into company_address) VALUES (ROW('London', 'UK'))