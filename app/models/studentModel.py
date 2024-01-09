from app import mysql

class StudentModel:
    # Get ALL STUDENTS  
    @classmethod
    def get_students(cls):
        try:
            cur = mysql.connection.cursor()
            sql = '''SELECT * FROM student ORDER BY student_id ASC'''
            cur.execute(sql)
            student = cur.fetchall()
            return student
        except Exception as e:
            return f"Failed to load Student List: {str(e)}"
        
    @classmethod
    def add_student(cls, id, firstname, lastname, year, gender, course):
        try:
            cur = mysql.connection.cursor()
            cur.execute(
                "INSERT INTO `student` (`student_id`, `firstname`, `lastname`, `year`, `gender`, `course_id`) VALUES (%s, %s, %s, %s, %s, %s)",
                (id, firstname, lastname, year, gender, course),
            )
            mysql.connection.commit()
            return "Faculty created successfully!"
        except Exception as e:
            return f"Failed to create College: {str(e)}"