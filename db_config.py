from dotenv import load_dotenv
import mysql.connector
import os

load_dotenv()

class Database:
    def __init__(self):
      try:
         self.mydb = mysql.connector.connect(
          host=os.environ.get('HOST'),
          user=os.environ.get('USER'),
          password=os.environ.get('PASSWORD'),
          database=os.environ.get('DATABASE_NAME'),
          port="3306"
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