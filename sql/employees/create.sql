CREATE DATABASE company
\c company

CREATE TABLE employees (id SERIAL PRIMARY KEY, name VARCHAR(255), surname VARCHAR(255), salary INT)

CREATE TABLE department (id SERIAL PRIMARY KEY, dep_name VARCHAR(255))

CREATE TABLE dep_emp (
                    id SERIAL PRIMARY KEY,
                    emp_id INTEGER REFERENCES employees (id),
                    manager_id INTEGER REFERENCES employees (id),
                    dep_id INTEGER REFERENCES department (id)
                    )
