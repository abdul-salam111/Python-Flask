import mysql.connector

class user_model():
    def __init__(self):
        # Make connection first with SQL
        try:
            self.con = mysql.connector.connect(host="localhost", user="root", password="", database="flask_project")
            print("connected to sql")
            self.cur = self.con.cursor(dictionary=True)  # Corrected this line
        except Exception as e:
            print(f"some error: {e}")
      
    def user_getall_model(self):
        self.cur.execute("select * from users")  # Corrected this line
        result = self.cur.fetchall()
        print(result)
        return "this is user signup model"
