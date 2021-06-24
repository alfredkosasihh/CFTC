import mysql.connector
from datetime import date
from utils.config import host, user, password, table

class initialize():
    def __init__(self):
        mydb = mysql.connector.connect(
            host = host,
            user = user,
            password = password,
        )
        mycursor = mydb.cursor() 
        mycursor.execute("CREATE DATABASE "+table+"")

class database():
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host = host,
            user = user,
            password = password,
            database = table
        )
        
    def create(self, db_name):
        mycursor = self.mydb.cursor() 
        mycursor.execute("""
            CREATE TABLE %s (
                date DATE NOT NULL, 
                long_val DECIMAL(10) NOT NULL, 
                short_val DECIMAL(10) NOT NULL, 
                change_long DECIMAL(10) NOT NULL, 
                change_short DECIMAL(10) NOT NULL,
                net_possition DECIMAL(10) NOT NULL)
        """%(db_name))
    
    def store(self, types, data=''):
        mycursor = self.mydb.cursor()
        mycursor.execute("""
                INSERT INTO """+types+"""  
                (date, long_val, short_val, change_long, change_short, net_possition ) 
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            ,(data[0], data[1], data[2], data[3], data[4], data[5])
        )
    
    def get(self, code):
        tmp_data = []
        
        mycursor = self.mydb.cursor()
        mycursor.execute("select * from "+code+" limit 12")

        for row in mycursor:
            tmp_data.append({
                'date': str(row[0]),
                'long': str(row[1]),
                'short': str(row[2]),
                'change_long': str(row[3]),
                'change_short': str(row[4]),
                'net_possition': str(row[5])
            })
        return{
            'result': '0',
            'result': "",
            'data': tmp_data
        }