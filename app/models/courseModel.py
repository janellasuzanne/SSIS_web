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

    # Get College List; Return College Codes only
    @classmethod
    def get_college_codes(cls):
        try:
            cur = mysql.connection.cursor()
            cur.execute(
                '''SELECT college_code, college_code FROM college'''
            )
            collegeCodes = cur.fetchall()
            cur.close()
            return collegeCodes
        except Exception as e:
            print(f"Failed to load College Codes: {str(e)}")
            return []
        
        
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
        
    @classmethod
    def delete_course(cls, course_code):
        try:
            cur = mysql.connection.cursor()
            cur.execute(
                "DELETE FROM `course` WHERE `course_code` = %s", 
                (course_code,)
            )
            mysql.connection.commit()
            return "Course deleted successfully!"
        except Exception as e:
            return f"Failed to delete course: {str(e)}"