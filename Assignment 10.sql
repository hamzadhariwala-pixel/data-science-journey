 CREATE TABLE Employees (
   EmpID INT PRIMARY KEY,
   Name VARCHAR(50),
   Department VARCHAR(50),
   Email VARCHAR(50)
 );
 INSERT INTO Employees (EmpID, Name, Department, Email) VALUES
   (1, 'Alice Johnson',  'HR',      'alice.johnson@example.com'),
   (2, 'Bob Smith',  	'IT',      'bob.smith@example.com'),
   (3, 'Charlie Brown',  'Finance','charlie.brown@example.com'),
   (4, 'Diana Prince',   'HR',      'diana.prince@example.com'),
   (5, 'Eve Adams',  	'IT',      'eve.adams@example.org');

--Listing employees with emails in the example.com domain.
SELECT Name, Email FROM Employees WHERE Email LIKE '%@example.com';


--Selecting employees whose names start with 'A'.
SELECT Name FROM Employees WHERE Name LIKE 'A%';


--Finding employees whose names end with 'son'.
SELECT Name FROM Employees WHERE Name LIKE '%son';


--Retrieving employees whose second character in the name is 'v'.
SELECT Name FROM Employees WHERE SUBSTRING(Name, 2, 1) = 'v';


--Selecting employees in departments containing 'IT'.
SELECT Name, Department FROM Employees WHERE Department LIKE '%IT%';


--Finding employees in departments with 'hr' regardless of case.
 SELECT Name, Department FROM Employees WHERE LOWER(Department) LIKE '%hr%';

