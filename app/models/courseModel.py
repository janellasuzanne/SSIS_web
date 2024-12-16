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
    def get_course_codes(cls):
        try:
            cur = mysql.connection.cursor()
            cur.execute(
                '''SELECT course_code, course_name FROM course'''
            )
            courseCodes = cur.fetchall()
            cur.close()
            return courseCodes
        except Exception as e:
            print(f"Failed to load Courses: {str(e)}")
            return []
        
    @classmethod
    def get_courses_by_college(cls, collegeId):
        try:
            cur = mysql.connection.cursor()
            cur.execute(
                '''SELECT course_code, course_name FROM course
                    WHERE college_id = %s''',
                    (collegeId,)
            )
            courses = cur.fetchall()
            course_choices = [(course[0], course[1]) for course in courses]
            return course_choices
        except Exception as e:
            print(f"Failed to fetch courses: {str(e)}")

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
    def update_course(cls, newCode, name, college, oldCode):
        try:
            if not newCode or not name or not oldCode:
                return "Cannot have empty fields!"
            
             # Custom validation for newCode
            if newCode.strip() == "" or not newCode.isalpha():
                return "College Code cannot be only spaces and should contain only letters."

            # Custom validation for name
            if name.strip() == "" or not all(c.isalpha() or c.isspace() for c in name):
                return "College Name should only contain letters and spaces."
            
            cur = mysql.connection.cursor()
            cur.execute(
                "UPDATE `course` SET `course_code` = %s, `course_name` = %s, `college_id` = %s WHERE `course_code` = %s",
                (newCode, name, college, oldCode),
            )
            mysql.connection.commit()
            return "College updated successfully!"
        except Exception as e:
            return f"Failed to update College: {str(e)}"
        
    @classmethod
    def search_course(cls, filter, input):
        try:
            cur = mysql.connection.cursor()
            if filter == "course_name":
                input = f'%{input}%'
                sql = f"SELECT * FROM course WHERE {filter} LIKE %s"
            else:
                sql = f"SELECT * FROM course WHERE {filter} = %s"
            cur.execute(sql, (input,))
            courses = cur.fetchall()
            cur.close()
            return courses
        except Exception as e:
            return f"Failed to fetch Courses: {str(e)}"