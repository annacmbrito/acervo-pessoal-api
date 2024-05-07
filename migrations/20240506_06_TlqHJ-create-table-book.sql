-- Create table book
-- depends: 20240506_05_Ues94-create-table-subcategory

CREATE TABLE IF NOT EXISTS book
(
    id SERIAL PRIMARY KEY,
    name VARCHAR(32) NOT NULL,
	description TEXT NOT NULL,
	comment TEXT NOT NULL,
	rating INT NOT NULL,
	available BOOLEAN NOT NULL,
	author_id INT NOT NULL REFERENCES author(id),
	language_id INT NOT NULL REFERENCES language(id),
	category_id INT NOT NULL REFERENCES category(id),
	subcategory_id INT NOT NULL REFERENCES subcategory(id)
);