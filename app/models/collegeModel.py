from app import mysql

class CollegeModel:
    # Get ALL COLLEGES  
    @classmethod
    def get_colleges(cls):
        try:
            cur = mysql.connection.cursor()
            sql = '''SELECT * FROM college'''
            cur.execute(sql)
            colleges = cur.fetchall()
            return colleges
        except Exception as e:
            return f"Failed to load College List: {str(e)}"
        
    # Get College by College Code
    @classmethod
    def get_single_college(cls, code):
        try:
            cur = mysql.connection.cursor()
            cur.execute("SELECT college_name FROM college WHERE college_code = %s",
            (code),
            )
            college = cur.fetchall()
            return college
        except Exception as e:
            return f"Faile to get college: {str(e)}"
    
    # Get College by Course Code
    @classmethod
    def get_college_by_course_name(cls, course_name):
        try:
            cur = mysql.connection.cursor()
            cur.execute('''SELECT `college_code` FROM `college` AS `clg`
                        LEFT JOIN `course` AS `crs`
                        ON `college_code` = `college_id`
                        WHERE `course_name` = %s''',
                        (course_name,)
                        )
            college = cur.fetchall()
            return college
        except Exception as e:
            return f"Failed to get college: {str(e)}"
                
    # Get College List; Return College Codes only
    @classmethod
    def get_college_codes(cls):
        try:
            cur = mysql.connection.cursor()
            cur.execute(
                '''SELECT college_code, college_name FROM college'''
            )
            collegeCodes = cur.fetchall()
            cur.close()
            return collegeCodes
        except Exception as e:
            print(f"Failed to load College Codes: {str(e)}")
            return []
        
    @classmethod
    def add_college(cls, code, name):
        try:
            cur = mysql.connection.cursor()
            cur.execute(
                "INSERT INTO `college` (`college_code`, `college_name`) VALUES (%s, %s)",
                (code, name),
            )
            mysql.connection.commit()
            return "College created successfully!"
        except Exception as e:
            return f"Failed to create College: {str(e)}"

    @classmethod
    def update_college(cls, code, name):
        try:
            cur = mysql.connection.cursor()
            cur.execute(
                "UPDATE `college` SET `college_name` = %s WHERE `college_code` = %s",
                (name, code),
            )
            mysql.connection.commit()
            return "College updated successfully!"
        except Exception as e:
            return f"Failed to update College: {str(e)}"

    @classmethod
    def delete_college(cls, college_code):
        try:
            cur = mysql.connection.cursor()
            cur.execute(
                "DELETE FROM `college` WHERE `college_code` = %s", 
                (college_code,)
            )
            mysql.connection.commit()
            return "College deleted successfully!"
        except Exception as e:
            return f"Failed to delete College: {str(e)}"
        
    @classmethod
    def search_college(cls, filter, input):
        try:
            cur = mysql.connection.cursor()
            sql = f"SELECT * FROM college WHERE {filter} = %s"
            cur.execute(sql, (input,))
            colleges = cur.fetchall()
            cur.close()
            return colleges
        except Exception as e:
            return f"Failed to fetch Colleges: {str(e)}"
