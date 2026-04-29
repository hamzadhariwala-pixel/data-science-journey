CREATE TABLE Orders (
   OrderID INT PRIMARY KEY,
   CustomerName VARCHAR(50),
   ProductCategory VARCHAR(50),
   Quantity INT,
   TotalPrice DECIMAL(10,2),
   OrderDate DATE
 );  --creates a table according to need.
INSERT INTO Orders (OrderID, CustomerName, ProductCategory, Quantity, TotalPrice, OrderDate) VALUES   --Inserts below values to the table created.
   (1, 'Alice',   'Electronics', 2,  1600.00, '2024-11-01'),
   (2, 'Bob', 	'Furniture',   1,   300.00, '2024-11-02'),
   (3, 'Charlie', 'Electronics', 1,   800.00, '2024-11-03'),
   (4, 'Diana',   'Stationery', 10,	50.00, '2024-11-04'),
   (5, 'Eve', 	'Electronics', 3,  2400.00, '2024-11-05'),
   (6, 'Frank',   'Stationery', 20,   100.00, '2024-11-06');


SELECT ProductCategory,SUM(Quantity)AS Total_Quantity FROM Orders GROUP BY ProductCategory;  --selects product category and the sum of its quantity from the main table and then grouping it according to the category

 SELECT ProductCategory
 FROM (
   SELECT ProductCategory, SUM(Quantity) AS TotalQuantity
   FROM Orders
   GROUP BY ProductCategory
 ) AS T
 WHERE TotalQuantity > 10;  -- this query is an extension of the above query to basically represent the category with high sales volume.

 SELECT ProductCategory, AVG(TotalPrice) AS AvgPrice
 FROM Orders
 GROUP BY ProductCategory;  -- this query gives the average price of a particular product in an orderly fashion.

  SELECT ProductCategory
 FROM (
   SELECT ProductCategory, AVG(TotalPrice) AS AvgPrice
   FROM Orders
   GROUP BY ProductCategory
 ) AS T
 WHERE AvgPrice < 1000; -- this query is an extension of the above query and gives us the names of the categories with low average price.

 SELECT *,
   CASE WHEN TotalPrice > 1000 THEN 'High Value'
    	ELSE 'Low Value'
   END AS ValueCategory
 FROM Orders; -- this query classifies between high value products and low value products.



  