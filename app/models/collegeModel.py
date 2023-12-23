from app import mysql

class CollegeModel:
    # Get ALL COLLEGES  
    @classmethod
    def get_colleges(cls):
        try:
            cur = mysql.connection.cursor()
            sql = '''SELECT * FROM college'''
            cur.execute(sql)
            college = cur.fetchall()
            return college
        except Exception as e:
            return f"Failed to load College List: {str(e)}"