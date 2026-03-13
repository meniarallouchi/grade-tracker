import database
import csv

def showMenu():
    print("\n--- Grade Tracker ---")
    print("1. Add student")
    print("2. Add course")
    print("3. Add grade")
    print("4. View all students")
    print("5. View all courses")
    print("6. View class average")
    print("7. View top performers")
    print("8. Export report to CSV")
    print("9. Exit")

def main():
    while True:
        showMenu()
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Student name: ")
            email = input("Student email: ")
            database.addStudent(name, email)
            print("Student added.")

        elif choice == "2":
            courseName = input("Course name: ")
            teacher = input("Teacher name: ")
            database.addCourse(courseName, teacher)
            print("Course added.")

        elif choice == "3":
            students = database.getStudents()
            print("\nStudents:")
            for s in students:
                print(f"  {s[0]}. {s[1]}")
            studentId = int(input("Enter student ID: "))

            courses = database.getCourses()
            print("\nCourses:")
            for c in courses:
                print(f"  {c[0]}. {c[1]}")
            courseId = int(input("Enter course ID: "))

            grade = float(input("Enter grade (0-100): "))
            database.addGrade(studentId, courseId, grade)
            print("Grade added.")

        elif choice == "4":
            students = database.getStudents()
            if not students:
                print("No students found.")
            for s in students:
                print(f"ID: {s[0]} | Name: {s[1]} | Email: {s[2]}")

        elif choice == "5":
            courses = database.getCourses()
            if not courses:
                print("No courses found.")
            for c in courses:
                print(f"ID: {c[0]} | Course: {c[1]} | Teacher: {c[2]}")

        elif choice == "6":
            courses = database.getCourses()
            for c in courses:
                print(f"  {c[0]}. {c[1]}")
            courseId = int(input("Enter course ID: "))
            avg = database.getClassAverage(courseId)
            if avg:
                print(f"Class average: {avg:.2f}")
            else:
                print("No grades found for this course.")

        elif choice == "7":
            topStudents = database.getTopPerformers()
            if not topStudents:
                print("No data yet.")
            else:
                print("\nTop performers:")
                for i, s in enumerate(topStudents, 1):
                    print(f"  {i}. {s[0]} - {s[1]:.2f}")

        elif choice == "8":
            reportData = database.getFullReport()
            if not reportData:
                print("No data to export.")
            else:
                with open("report.csv", "w", newline="") as f:
                    writer = csv.writer(f)
                    writer.writerow(["Student", "Course", "Grade"])
                    writer.writerows(reportData)
                print("Report saved to report.csv")

        elif choice == "9":
            print("Bye!")
            break

        else:
            print("Invalid option, try again.")

main()
