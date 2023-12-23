from app import mysql

class StudentModel:
    # Get ALL STUDENTS  
    @classmethod
    def get_students(cls):
        try:
            cur = mysql.connection.cursor()
            sql = '''SELECT * FROM student ORDER BY year, student_id ASC'''
            cur.execute(sql)
            student = cur.fetchall()
            return student
        except Exception as e:
            return f"Failed to load Student List: {str(e)}"