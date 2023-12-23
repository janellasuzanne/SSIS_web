from app import mysql

class CourseModel:
    # Get ALL COURSES  
    @classmethod
    def get_courses(cls):
        try:
            cur = mysql.connection.cursor()
            sql = '''SELECT * FROM course ORDER BY college_id'''
            cur.execute(sql)
            course = cur.fetchall()
            return course
        except Exception as e:
            return f"Failed to load Course List: {str(e)}"