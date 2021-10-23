-- casting 
SELECT 
  CAST('10' as INTEGER)

SELECT 
  CAST('true' AS BOOLEAN),
  CAST('01-May-2020' AS DATE),
  CAST('14.12345' AS DOUBLE PRECISION),
  '10'::INTEGER

SELECT 
	id,
	CASE
		WHEN rating~E'^\\d+$' THEN
			CAST (rating AS INTEGER)
		ELSE
			0
		END as rating
FROM
	ratings;