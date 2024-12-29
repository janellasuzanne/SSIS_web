from app import mysql

class StudentModel:
    # Get ALL STUDENTS  
    @classmethod
    def get_students(cls):
        try:
            cur = mysql.connection.cursor()
            cur.execute(
                "SELECT * FROM `student` ORDER BY `year` DESC"
            )
            students = cur.fetchall()
            return students
        except Exception as e:
            return f"Failed to load Student List: {str(e)}"
        
    @classmethod
    def get_single_student(cls, id):
        try:
            cur = mysql.connection.cursor()
            cur.execute(
                "SELECT * FROM `student` WHERE student_id = %s",
                (id,)
            )
            student = cur.fetchall()
            cur.close()
            return student
        except Exception as e:
            return f"Failed to fetch student: {str(e)}"
        
    @classmethod
    def get_profile_url(cls, id):
        try:
            cur = mysql.connection.cursor()
            cur.execute(
                "SELECT `profile_pic` FROM `student` WHERE student_id = %s",
                (id,)
            )
            profile_url = cur.fetchall()
            cur.close()
            return str(profile_url)
        except Exception as e:
            return f"Failed to fetch student's profile id: {str(e)}"
        
    @classmethod
    def add_student(cls, id, firstname, lastname, course, year, gender, profile_pic):
        try:
            cur = mysql.connection.cursor()
            cur.execute(
                "INSERT INTO `student` (`student_id`, `firstname`, `lastname`, `student_course`, `year`, `gender`, `profile_pic`) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                (id, firstname, lastname, course, year, gender, profile_pic,)
            )
            mysql.connection.commit()
            return "Student created successfully!"
        except Exception as e:
            return f"Failed to create student: {str(e)}"
        
    @classmethod
    def update_student(cls, id, firstname, lastname, course, year, gender, profile_pic):
        try:
            if not firstname or not lastname:
                return "Student not updated: Cannot have empty fields!"
            
            if firstname.strip() == "" or not all(c.isalpha() or c.isspace() for c in firstname):
                return "Student not updated: First Name should only contain letters and spaces."
            
            if lastname.strip() == "" or not all(c.isalpha() or c.isspace() for c in lastname):
                return "Student not updated: Last Name should only contain letters and spaces."
            
            if not profile_pic:
                return "Student not updated: Invalid profile photo."
            
            cur = mysql.connection.cursor()
            cur.execute(
                '''UPDATE `student`
                    SET `student_id` = %s,
                        `firstname` = %s,
                        `lastname` = %s,
                        `student_course` = %s,
                        `year` = %s,
                        `gender` = %s,
                        `profile_pic` = %s
                    WHERE `student_id` = %s''',
                    (id, firstname, lastname, course, year, gender, profile_pic, id),
            )
            mysql.connection.commit()
            return "Student updated successfully!"
        except Exception as e:
            return f"Failed to update Student: {str(e)}"
        
    @classmethod
    def delete_student(cls, id):
        try:
            cur = mysql.connection.cursor()
            cur.execute(
                "DELETE FROM `student` WHERE student_id = %s",
                (id,)
            )
            mysql.connection.commit()
            return "Student deleted successfully!"
        except Exception as e:
            return f"Failed to delete student: {str(e)}"
        
    @classmethod
    def search_student(cls, filter, input):
        try:
            cur = mysql.connection.cursor()
            if filter == "student_course":
                input = f'%{input}%'
                sql = f"SELECT * FROM student WHERE {filter} LIKE %s"
            else:
                sql = f"SELECT * FROM student WHERE {filter} = %s"
            cur.execute(sql, (input,))
            students = cur.fetchall()
            cur.close()
            return students
        except Exception as e:
            return f"Failed to fetch Students: {str(e)}"