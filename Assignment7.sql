 -- Employees table
 CREATE TABLE Employees (
   EmpID INT PRIMARY KEY,
   EmpName VARCHAR(50),
   DepartmentID INT
 );
 INSERT INTO Employees (EmpID, EmpName, DepartmentID) VALUES
   (1, 'Alice',   101),
   (2, 'Bob', 	102),
   (3, 'Charlie', 103),
   (4, 'Diana',   NULL),
   (5, 'Eve', 	101);

  -- Departments table
 CREATE TABLE Departments (
   DepartmentID INT PRIMARY KEY,
   DeptName VARCHAR(50),
   Location VARCHAR(50)
 );
 INSERT INTO Departments (DepartmentID, DeptName, Location) VALUES
   (101, 'HR',   	'New York'),
   (102, 'IT',   	'San Francisco'),
   (103, 'Finance',  'Chicago'),
   (104, 'Sales',	'Boston');

-- performing inner join, i.e., returning the rows which are present in both tables.
SELECT E.EmpID, E.EmpName, D.DeptName
 FROM Employees E
 INNER JOIN Departments D
   ON E.DepartmentID = D.DepartmentID;

-- performing left join, i.e., returning all rows from left table(table1) aka employees.
SELECT E.EmpID, E.EmpName, D.DeptName
 FROM Employees E
 LEFT JOIN Departments D
   ON E.DepartmentID = D.DepartmentID;

-- performing right join, i.e., returning all rows from right table(table2) aka departments.
SELECT D.DepartmentID, D.DeptName, E.EmpName
 FROM Employees E
 RIGHT JOIN Departments D
   ON E.DepartmentID = D.DepartmentID;

-- performing full outer join, i.e., returning all rows from both the tables, matching where possible.
 SELECT E.EmpID, E.EmpName, D.DeptName
 FROM Employees E
 FULL OUTER JOIN Departments D
   ON E.DepartmentID = D.DepartmentID;

--performing cross join,i.e., Generating every combination of employee names and department names.
 SELECT E.EmpName, D.DeptName
 FROM Employees E
 CROSS JOIN Departments D;

-- performing union all function,i.e., Creating a list combining all employee names and department names in one column.
SELECT EmpName AS Name FROM Employees
 UNION ALL
 SELECT DeptName FROM Departments;

--performing intersect function, i.e, Finding department IDs present in both tables.
SELECT DepartmentID FROM Employees
 INTERSECT
 SELECT DepartmentID FROM Departments;

-- performing except function, i.e, Listing department IDs in Departments but not in Employees.
SELECT DepartmentID FROM Departments
 EXCEPT
 SELECT DepartmentID FROM Employees;
