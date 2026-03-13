import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

def getConnection():
    conn = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )
    return conn

def addStudent(name, email):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, email) VALUES (%s, %s)", (name, email))
    conn.commit()
    conn.close()

def addCourse(courseName, teacher):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO courses (courseName, teacher) VALUES (%s, %s)", (courseName, teacher))
    conn.commit()
    conn.close()

def addGrade(studentId, courseId, grade):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO grades (studentId, courseId, grade) VALUES (%s, %s, %s)", (studentId, courseId, grade))
    conn.commit()
    conn.close()

def getStudents():
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    result = cursor.fetchall()
    conn.close()
    return result

def getCourses():
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM courses")
    result = cursor.fetchall()
    conn.close()
    return result

def getClassAverage(courseId):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute("SELECT AVG(grade) FROM grades WHERE courseId = %s", (courseId,))
    result = cursor.fetchone()
    conn.close()
    return result[0]

def getTopPerformers():
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT s.name, AVG(g.grade) as avgGrade
        FROM students s
        JOIN grades g ON s.studentId = g.studentId
        GROUP BY s.studentId
        ORDER BY avgGrade DESC
        LIMIT 5
    """)
    result = cursor.fetchall()
    conn.close()
    return result

def getFullReport():
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT s.name, c.courseName, g.grade
        FROM grades g
        JOIN students s ON g.studentId = s.studentId
        JOIN courses c ON g.courseId = c.courseId
        ORDER BY s.name
    """)
    result = cursor.fetchall()
    conn.close()
    return result
