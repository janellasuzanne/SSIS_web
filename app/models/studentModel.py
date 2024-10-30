from app import mysql

class StudentModel:
    # Get ALL STUDENTS  
    @classmethod
    def get_students(cls):
        try:
            cur = mysql.connection.cursor()
            cur.execute(
                "SELECT * FROM `student` ORDER BY `student_id` ASC"
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
            mysql.connection.commit()
            return "Student fetched successfully!"
        except Exception as e:
            return f"Failed to fetch student: {str(e)}"
        
    @classmethod
    def add_student(cls, id, firstname, lastname, course, year, gender):
        try:
            cur = mysql.connection.cursor()
            cur.execute(
                "INSERT INTO `student` (`student_id`, `firstname`, `lastname`, `course_id`, `year`, `gender`) VALUES (%s, %s, %s, %s, %s, %s)",
                (id, firstname, lastname, course, year, gender,)
            )
            mysql.connection.commit()
            return "Student created successfully!"
        except Exception as e:
            return f"Failed to create College: {str(e)}"
        
    @classmethod
    def update_student(cls, id, firstname, lastname, course, year, gender):
        try:
            cur = mysql.connection.cursor()
            cur.execute(
                '''UPDATE `student`
                    SET `student_id` = %s,
                        `firstname` = %s,
                        `lastname` = %s,
                        `course_id` = %s,
                        `year` = %s,
                        `gender` = %s
                    WHERE `student_id` = %s''',
                    (id, firstname, lastname, course, year, gender, id),
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
            sql = f"SELECT * FROM student WHERE {filter} = %s"
            cur.execute(sql, (input,))
            students = cur.fetchall()
            cur.close()
            return students
        except Exception as e:
            return f"Failed to fetch Students: {str(e)}"