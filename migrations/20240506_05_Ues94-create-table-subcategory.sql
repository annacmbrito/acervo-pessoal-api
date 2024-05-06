-- Create table subcategory
-- depends: 20240506_04_eKnVi-create-table-category

CREATE TABLE IF NOT EXISTS subcategory
(
    id SERIAL PRIMARY KEY,
    name VARCHAR(32) NOT NULL,
	category_id INT NOT NULL 
        REFERENCES category(id)
        ON DELETE CASCADE
);
