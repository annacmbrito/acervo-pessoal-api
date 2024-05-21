-- Create table book
-- depends: 20240506_05_Ues94-create-table-subcategory

CREATE TABLE IF NOT EXISTS book
(
    id SERIAL PRIMARY KEY,
    name VARCHAR(128) NOT NULL,
	description TEXT,
	comment TEXT,
	rating INT,
	pages INT,
	status VARCHAR(32),
	author_id INT REFERENCES author(id),
	language_id INT REFERENCES language(id),
	publisher_id INT REFERENCES publisher(id),
	category_id INT REFERENCES category(id),
	subcategory_id INT REFERENCES subcategory(id)
);
