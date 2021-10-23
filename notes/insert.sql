-- simple insert
INSERT INTO t_tags (tag) VALUES 
('Pen'),
('Pencil');

-- insert with conflict check, do nothing
INSERT INTO t_tags (tag) VALUES ('Pen')
ON conflict (tag) Do nothing

-- insert with conflict check, do update
INSERT INTO t_tags (tag) VALUES ('Pen')
ON CONFLICT (tag) Do 
  UPDATE SET 

-- insert with type explict conversion
-- convert the '1' to 1
SELECT * FROM movies 
WHERE movie_id = integer '1'



