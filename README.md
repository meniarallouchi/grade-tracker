# Student Grade Tracker

Python CLI app to manage students, courses, and grades using MySQL. Supports class averages, top performers, and CSV report exports.

## Built With

- [Python 3](https://www.python.org/)
- [MySQL](https://www.mysql.com/) - relational database management system
- [mysql-connector-python](https://pypi.org/project/mysql-connector-python/) - database connection and queries
- [python-dotenv](https://pypi.org/project/python-dotenv/) - environment variable management

## Getting Started

### Prerequisites

Make sure you have Python 3 and MySQL installed, then install the dependencies:

```
pip install mysql-connector-python python-dotenv
```

### Usage

1. Clone the repo
```
git clone https://github.com/meniarallouchi/grade-tracker
```
2. Create a `.env` file in the project folder using `.env.example` as a template:
```
DB_HOST=
DB_USER=
DB_PASSWORD=
DB_NAME=
```
3. Run `schema.sql` in your MySQL client to set up the database, or from the terminal:
```
mysql -u root -p < schema.sql
```
4. Run the app
```
python main.py
```

## Schema Overview

Table       | Description
------------|------------------------------------------------------
`students`  | Stores student name and email
`courses`   | Stores course name and teacher
`grades`    | Links students to courses with a grade value, foreign keys to both tables

## How It Works

1. Students and courses are added independently then linked through the `grades` table
2. Foreign key constraints ensure grades can only reference existing students and courses
3. Class averages are calculated using SQL `AVG()` grouped by course
4. Top performers are ranked by averaging all grades per student across all courses
5. The full report query joins all three tables and can be exported to a `.csv` file
