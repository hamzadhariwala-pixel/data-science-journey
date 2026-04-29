CREATE TABLE Employees (
   EmpID INT PRIMARY KEY,
   Name VARCHAR(50),
   DateOfBirth DATE,
   JoinDate DATE
 );
 INSERT INTO Employees (EmpID, Name, DateOfBirth, JoinDate) VALUES
   (1, 'Alice Johnson', '1985-05-20', '2010-06-15'),
   (2, 'Bob Smith', 	'1990-08-10', '2015-09-01'),
   (3, 'Charlie Brown', '1988-03-25', '2012-11-12'),
   (4, 'Diana Prince',  '1992-01-30', '2017-07-08'),
   (5, 'Eve Adams', 	'1987-12-05', '2013-03-20');

--Displaying the current system date and time.
 SELECT CURRENT_TIMESTAMP;


-- Computing each employee’s age in years based on DateOfBirth.
SELECT Name, FLOOR(Extract(Year from age(CURRENT_DATE, DateOfBirth))) as Age FROM Employees;


--Computing total years of service since JoinDate.
SELECT Name, FLOOR(Extract(Year from age(CURRENT_DATE, JoinDate))) AS YearsExperience FROM Employees;


--Extracting year, month, and day from DateOfBirth.
 SELECT Name, Extract (YEAR from DateOfBirth) AS BirthYear, 
 Extract(MONTH from DateOfBirth) AS BirthMonth, Extract (DAY from DateOfBirth) AS BirthDay FROM Employees;


--Listing employees born in the month of August.
 SELECT Name FROM Employees WHERE Extract (MONTH from DateOfBirth) = 8;


 --Displaying names of employees whose birthdays fall in the next 30 days.
SELECT Name FROM Employees
WHERE (DATE_TRUNC('year', CURRENT_DATE) + (DateOfBirth - DATE_TRUNC('year',DateOfBirth)))
    BETWEEN CURRENT_DATE AND CURRENT_DATE + INTERVAL '30 days';
