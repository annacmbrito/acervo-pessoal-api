-- Create table publisher 
-- depends: 20240506_05_Ues94-create-table-subcategory

CREATE TABLE IF NOT EXISTS publisher(
	id SERIAL PRIMARY KEY,
    name VARCHAR(32) NOT NULL
)
