 CREATE TABLE Orders (
   OrderID INT PRIMARY KEY,
   OrderDate DATE,
   Amount DECIMAL(10,2)
 );
 INSERT INTO Orders (OrderID, OrderDate, Amount) VALUES
   (1, '2024-11-01', 250.50),
   (2, '2024-11-02', 300.75),
   (3, '2024-11-03', 150.25);


--Converting the Amount column to a textual string.
SELECT CAST(Amount AS CHAR(10)) AS AmountText FROM Orders;


-- Formatting OrderDate as a string (e.g., 'YYYY-MM-DD').
SELECT To_Char(OrderDate, 'yyyy-MM-dd') AS OrderDateText FROM Orders;


--Converting literal '2024-11-05' into a DATE type.
SELECT CAST('2024-11-05' AS DATE) AS ConvertedDate;


--Retrieving the year component from OrderDate.
SELECT Extract(YEAR from (OrderDate)) AS OrderYear FROM Orders;


--Combining OrderDate and Amount into one string.
SELECT CONCAT(To_Char(OrderDate, 'YYYY-MM-DD'), ' - $', Amount) AS Summary FROM Orders;
