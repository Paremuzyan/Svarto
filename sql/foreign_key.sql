local   all   postgres   peer

drop table student;
drop table course;

\c anahit
Create table student(id serial primary key, full_name varchar(50), age int);
Create table course(id serial primary key, name varchar(50), price int);
create table std_courses(id serial primary key, student_id integer references student(id), course_id integer references course(id));
insert into student (full_name, age) values ('student_1', 17), ('student_2', 18);
insert into course (name, price) values ('Python', 20000), ('C++', 30000);
insert into std_courses (student_id, course_id) values (1,1),(1,2), (2,1);
select
    student.full_name as studetn,
    student.age,
    course.name as course_name,
    course.price as cource_price
    from std_courses
    join student on std_courses.student_id=student.id
    join course on std_courses.course_id=course.id;