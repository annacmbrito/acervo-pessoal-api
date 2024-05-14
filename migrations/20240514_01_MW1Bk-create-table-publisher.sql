-- Create table publisher 
-- depends: 20240506_06_TlqHJ-create-table-book

CREATE TABLE IF NOT EXISTS publisher(
	id SERIAL PRIMARY KEY,
    name VARCHAR(32) NOT NULL
)
