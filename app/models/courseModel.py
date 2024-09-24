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
    def get_courses_by_college(cls, collegeName):
        try:
            cur = mysql.connection.cursor()
            cur.execute(
                '''SELECT course_code, course_name FROM `course`
                    LEFT JOIN `college`
                    ON course.college_id = college.college_code
                    WHERE college.college_name = %s''',
                    (collegeName),
            )
            mysql.connection.commit()
            return "Courses fetched successfully!"
        except Exception as e:
            return f"Failed to fetch courses: {str(e)}"
    
        
    @classmethod
    def add_course(cls, collegeId, code, name):
        try:
            cur = mysql.connection.cursor()
            cur.execute(
                "INSERT INTO `course` (`course_code`, `course_name`, `college_id`) VALUES (%s, %s, %s)",
                (code, name, collegeId),
            )
            mysql.connection.commit()
            return "Course created successfully!"
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
        
    @classmethod
    def update_course(cls, code, name):
        try:
            cur = mysql.connection.cursor()
            cur.execute(
                "UPDATE `course` SET `course_name` = %s WHERE `course_code` = %s",
                (name, code),
            )
            mysql.connection.commit()
            return "College updated successfully!"
        except Exception as e:
            return f"Failed to update College: {str(e)}"