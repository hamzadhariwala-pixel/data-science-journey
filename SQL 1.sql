CREATE TABLE EMPLOYEES (
	EMP_ID INT,
	NAME VARCHAR(50),
	DEPARTMENT VARCHAR(50),
	SALARY INT,
	CITY VARCHAR(50),
	JOINING_YEAR INT
);

INSERT INTO
	EMPLOYEES
VALUES
	(1, 'Ali', 'Sales', 50000, 'Pune', 2020),
	(2, 'Sara', 'HR', 60000, 'Mumbai', 2019),
	(3, 'Omar', 'IT', 75000, 'Pune', 2021),
	(4, 'Zara', 'IT', 80000, 'Mumbai', 2018),
	(5, 'Ayaan', 'Sales', 45000, 'Delhi', 2022),
	(6, 'Fatima', 'HR', 52000, 'Pune', 2020),
	(7, 'Rehan', 'IT', 90000, 'Delhi', 2017),
	(8, 'Noor', 'Sales', 47000, 'Mumbai', 2023);

SELECT
	*
FROM
	EMPLOYEES
WHERE
	CITY = 'Pune';

SELECT
	*
FROM
	EMPLOYEES
WHERE
	SALARY > 60000;

SELECT
	*
FROM
	EMPLOYEES
WHERE
	JOINING_YEAR > 2020;

SELECT
	*
FROM
	EMPLOYEES
WHERE
	DEPARTMENT = 'IT';

SELECT
	*
FROM
	EMPLOYEES
ORDER BY
	SALARY DESC;

SELECT
	*
FROM
	EMPLOYEES
ORDER BY
	JOINING_YEAR ASC;

SELECT
	*
FROM
	EMPLOYEES
WHERE
	SALARY > 50000
	AND CITY = 'Pune';

SELECT
	*
FROM
	EMPLOYEES
WHERE
	CITY <> 'Mumbai';

SELECT
	*
FROM
	EMPLOYEES
WHERE
	NAME LIKE 'A%';

SELECT
	*
FROM
	EMPLOYEES
WHERE
	SALARY > 50000
	AND SALARY < 80000;

SELECT department, SUM(salary)
FROM employees
GROUP BY department;
SELECT city, AVG(salary)
FROM employees
GROUP BY city;

SELECT department, COUNT(*)
FROM employees
GROUP BY department;

select department, max(salary)
from employees
group by departm