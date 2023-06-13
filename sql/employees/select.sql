--Retrieve the full name, department, and salary of all employees.

SELECT  employees.name,
        employees.surname,
        employees.salary,
        employees.name,
        employees.surname,
        department.dep_name
        FROM dep_emp
        JOIN employees ON dep_emp.emp_id=employees.id
        JOIN department ON dep_emp.dep_id=department.id;

--Retrieve the department name and the average salary of all employees in each department.

SELECT department.dep_name, AVG(employees.salary) AS average_salary
FROM dep_emp
JOIN employees ON dep_emp.emp_id = employees.id
JOIN department ON dep_emp.dep_id = department.id
GROUP BY department.dep_name;

--Retrieve the full name and manager name of all employees along with their respective departments.

SELECT CONCAT(e.name, ' ', e.surname) AS employee,
       CONCAT(m.name, ' ', m.surname) AS manager,
       d.dep_name AS department_name
FROM dep_emp de
JOIN employees e ON de.emp_id = e.id
JOIN department d ON de.dep_id = d.id
JOIN employees m ON de.manager_id = m.id;

--Retrieve the full name and email of all employees who have a salary greater than $50,000.

SELECT * FROM employees WHERE salary > 50000;

--Update the salary of an employee with a given employee ID.

UPDATE employees
SET salary = 60000
WHERE id = 1;

--Delete an employee with a given employee ID.

DELETE FROM employees where id = 4;
