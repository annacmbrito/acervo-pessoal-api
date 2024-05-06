-- Create table category
-- depends: 20240506_03_VjLlU-create-table-language

CREATE TABLE IF NOT EXISTS category
(
    id SERIAL PRIMARY KEY,
    name VARCHAR(32) NOT NULL
);
