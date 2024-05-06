-- Create table author
-- depends: 20240506_01_CFHsf-create-table-users

CREATE TABLE IF NOT EXISTS author
(
    id SERIAL PRIMARY KEY,
    name VARCHAR(32) NOT NULL
);
