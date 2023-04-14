import mysql.connector

class Database:
    def __init__(self):
      try:
         self.mydb = mysql.connector.connect(
          host="localhost",
          user="root",
          password="",
          database="python_restapi"
        )
         if self.mydb.is_connected():
            print("************Connected to the mysql database****************")

            self.mycursor = self.mydb.cursor()
         
      except mysql.connector.Error as e:
         print(e)
         exit()
      
      
      
      
      
      
        
   

# mycursor = mydb.cursor()

# db = Database()
# print(db.mydb)