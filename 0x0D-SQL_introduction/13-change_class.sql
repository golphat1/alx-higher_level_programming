-- Script removes all records with a score <= 5 in the table second_table

-- Delete scores with records less than 5
DELETE FROM second_table
WHERE second_table.score <= 5;
