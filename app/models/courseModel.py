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
        
    @classmethod
    def add_course(cls, collegeId, code, name):
        try:
            cur = mysql.connection.cursor()
            cur.execute(
                "INSERT INTO `course` (`course_code`, `course_name`, `college_id`) VALUES (%s, %s, %s)",
                (code, name, collegeId),
            )
            mysql.connection.commit()
            return "Faculty created successfully!"
        except Exception as e:
            return f"Failed to create College: {str(e)}"