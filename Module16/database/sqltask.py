import sqlite3


class UniversityDB:
    def __init__(self, name):
        self.name = name
        self.conn = sqlite3.connect('students.db')
        self.create_tables()

    def create_tables(self):
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    age INTEGER NOT NULL
                )
            ''')
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS grades (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    student_id INTEGER,
                    subject TEXT NOT NULL,
                    grade FLOAT NOT NULL,
                    FOREIGN KEY (student_id) REFERENCES students(id)
                )
            ''')

    def add_student(self, name, age):
        with self.conn:
            self.conn.execute('''
                INSERT INTO students (name, age) VALUES (?, ?)
            ''', (name, age))

    def add_grade(self, student_id, subject, grade):
        with self.conn:
            self.conn.execute('''
                INSERT INTO grades (student_id, subject, grade) VALUES (?, ?, ?)
            ''', (student_id, subject, grade))

    def get_students(self, subject=None):
        with self.conn:
            if subject:
                cursor = self.conn.execute('''
                    SELECT students.name, students.age, grades.subject, grades.grade 
                    FROM students 
                    JOIN grades ON students.id = grades.student_id
                    WHERE grades.subject = ?
                ''', (subject,))
            else:
                cursor = self.conn.execute('''
                    SELECT students.name, students.age, grades.subject, grades.grade 
                    FROM students 
                    JOIN grades ON students.id = grades.student_id
                ''')
            return cursor.fetchall()


u1 = UniversityDB('Urban')

u1.add_student('Ivan', 26)
u1.add_student('Ilya', 24)
u1.add_student('Anna', 22)
u1.add_student('Maria', 23)

u1.add_grade(1, 'Python', 4.8)
u1.add_grade(2, 'PHP', 4.3)
u1.add_grade(1, 'Math', 4.5)
u1.add_grade(2, 'Java', 3.9)
u1.add_grade(3, 'Python', 4.9)
u1.add_grade(3, 'Math', 4.7)
u1.add_grade(4, 'Java', 4.1)
u1.add_grade(4, 'PHP', 3.8)

print(u1.get_students())
print(u1.get_students('Python'))
