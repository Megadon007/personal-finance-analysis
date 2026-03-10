SELECT Type, 
       ROUND(SUM(Amount), 2) AS Total_Amount
FROM transactions
GROUP BY Type;


SELECT Category,
       ROUND(SUM(Amount), 2) AS Total_Expense
FROM transactions
WHERE Type = 'Expense'
GROUP BY Category
ORDER BY Total_Expense DESC;

SELECT Year,
       ROUND(SUM(Amount), 2) AS Total_Expense
FROM transactions
WHERE Type = 'Expense'
GROUP BY Year
ORDER BY Total_Expense DESC;



SELECT Month,
       ROUND(AVG(Amount), 2) AS Avg_Monthly_Expense
FROM transactions
WHERE Type = 'Expense'
GROUP BY Month
ORDER BY Avg_Monthly_Expense DESC;