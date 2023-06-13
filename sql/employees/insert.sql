INSERT INTO employees (name, surname, salary)
VALUES
    ('John', 'Doe', 50000),
    ('Jane', 'Smith', 60000),
    ('Michael', 'Johnson', 55000),
    ('Emily', 'Davis', 52000),
    ('Robert', 'Brown', 48000),
    ('Emma', 'Wilson', 65000),
    ('David', 'Taylor', 53000),
    ('Olivia', 'Miller', 57000),
    ('William', 'Anderson', 51000),
    ('Poghos', 'Poghosyan', 45000),
    ('Martiros', 'Martirosyan', 60000),
     ('Petros', 'Petrosyan', 50000),
    ('Sophia', 'Moore', 54000);


INSERT INTO department (dep_name)
VALUES
    ('Sales'),
    ('Marketing'),
    ('Finance'),
    ('Human Resources'),
    ('Operations');

INSERT INTO dep_emp (emp_id, manager_id, dep_id)
VALUES
    (1, 5, 2),
    (2, 5, 2),
    (8, 11, 3),
    (13, 11, 3);
