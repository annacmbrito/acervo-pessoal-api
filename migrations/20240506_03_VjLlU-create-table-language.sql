-- Create table language
-- depends: 20240506_02_fDfCn-create-table-author

CREATE TABLE IF NOT EXISTS language
(
    id SERIAL PRIMARY KEY,
    name VARCHAR(32) NOT NULL
);

