CREATE DATABASE IF NOT EXISTS gradeTracker;
USE gradeTracker;

CREATE TABLE IF NOT EXISTS students (
    studentId INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS courses (
    courseId INT AUTO_INCREMENT PRIMARY KEY,
    courseName VARCHAR(100),
    teacher VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS grades (
    gradeId INT AUTO_INCREMENT PRIMARY KEY,
    studentId INT,
    courseId INT,
    grade DECIMAL(5,2),
    FOREIGN KEY (studentId) REFERENCES students(studentId),
    FOREIGN KEY (courseId) REFERENCES courses(courseId)
);
