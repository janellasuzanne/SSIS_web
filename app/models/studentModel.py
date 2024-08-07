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
    def add_student(cls, id, firstname, lastname, year, gender, course):
        try:
            cur = mysql.connection.cursor()
            cur.execute(
                "INSERT INTO `student` (`student_id`, `firstname`, `lastname`, `year`, `gender`, `course_id`) VALUES (%s, %s, %s, %s, %s, %s)",
                (id, firstname, lastname, year, gender, course,)
            )
            mysql.connection.commit()
            return "Student created successfully!"
        except Exception as e:
            return f"Failed to create College: {str(e)}"
        
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