-- Create table image
-- depends: 20240514_01_MW1Bk-create-table-publisher

CREATE TABLE IF NOT EXISTS image
(
    id VARCHAR(64) PRIMARY KEY,
    url VARCHAR(255) NOT NULL
);