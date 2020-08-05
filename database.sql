create table student
(
    sid varchar primary key,
    fname varchar not null,
    lname varchar not null,
    dob date not null,
    age int not null,
    gender varchar not null,
    phno bigint not null,
    house_no varchar not null,
    building varchar not null,
    city varchar not null,
    course_id varchar not null references course,
    dept_id varchar not null references department
);

create table faculty
(
    fid varchar primary key,
    fname varchar not null,
    lname varchar not null,
    dob date not null,
    gender varchar not null,
    salary bigint not null,
    designation varchar not null,
    course_id varchar references course,
    dept_id varchar references department,
    project_id varchar references project
);


create table course
(
    course_id varchar primary key,
    name varchar not null
);

create table department
(
    dept_id varchar primary key,
    name varchar not null
);


create table project
(
    project_id varchar primary key,
    project_name varchar not null
);


create table per_project
(
    fid varchar references faculty,
    project_id varchar references project,
    start_date date not null,
    no_of_hours bigint not null
);