#for all data
SELECT *
FROM table1
INNER JOIN table2
ON table1.pk = table2.pk;


#if null data
SELECT column1, column2, ...
FROM table1
JOIN table2
ON table1.pk = table2.pk

WHERE (condition)
ORDER BY (value)

#inner join connects only returns connected matching rows

#full join returns connected rows and unconnected rows from both left and right tables