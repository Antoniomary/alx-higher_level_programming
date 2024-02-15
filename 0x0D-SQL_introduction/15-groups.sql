-- lists the number of records with the same score in the i
-- table second_table of the database hbtn_0c_0 in your MySQL server.

SELECT score, COUNT(name) AS number
FROM second_table
GROUP BY score;
