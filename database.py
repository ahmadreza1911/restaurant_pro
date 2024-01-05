import sqlite3
import os
from khayyam import *

class Database:
    def __init__(self,db) :
        self.__db_name= db
        self.connection= sqlite3.connect(db)
        self.cursor=self.connection.cursor()
        
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS [table_menu](
                                [ID] INT PRIMARY KEY NOT NULL UNIQUE, 
                                [name] NVARCHAR(40) NOT NULL UNIQUE, 
                                [price] INT NOT NULL,
                                [type_is_food] BOOL NOT NULL) WITHOUT ROWID;
                                
                            """)
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS [table_receipt]( 
                                [receipt_id] INT NOT NULL, 
                                [menu_id] INT NOT NULL REFERENCES [table_menu]([ID]), 
                                [count] INT,
                                [price] INT,
                                [date] TEXT NOT NULL, 
                                [daily_receipt_id] INT NOT NULL);
                                
                            """)
        self.cursor.execute("""CREATE VIEW IF NOT EXISTS view_menu_receipt AS
                                SELECT table_receipt.receipt_id, table_menu.name, table_receipt.count,
                                table_receipt.price, (table_receipt.price * table_receipt.count) AS sum
                                FROM table_menu
                                INNER JOIN table_receipt ON table_menu.ID == table_receipt.menu_id
                            """)
        
        self.connection.commit()
        self.connection.close()
    
    def insert(self,id,name,price,type_is_food):
        self.connection= sqlite3.connect(self.__db_name)
        self.cursor=self.connection.cursor()
        self.cursor.execute("INSERT INTO table_menu VALUES (? , ? , ? , ?)",(id, name, price,type_is_food) )
        self.connection.commit()
        self.connection.close()


    def get_menu_items(self,type_is_food):
        self.connection= sqlite3.connect(self.__db_name)
        self.cursor=self.connection.cursor()
        self.cursor.execute("SELECT * FROM table_menu WHERE type_is_food=?" , (type_is_food,))
        result = self.cursor.fetchall()
        return result


    def get_max_receipt(self):
        self.connection= sqlite3.connect(self.__db_name)
        self.cursor=self.connection.cursor()
        self.cursor.execute("SELECT MAX(receipt_id) FROM table_receipt")
        result = self.cursor.fetchall()
        return result  
    

    def get_menu_item_by_name(self,menu_item_name):
        self.connection= sqlite3.connect(self.__db_name)
        self.cursor=self.connection.cursor()
        self.cursor.execute("SELECT * FROM table_menu WHERE name=?" , (menu_item_name,))
        result = self.cursor.fetchall()
        return result
    

    def insert_into_receipt(self,receipt_id,menu_id,count,price,date,daily_receipt_id):
        self.connection= sqlite3.connect(self.__db_name)
        self.cursor=self.connection.cursor()
        self.cursor.execute("INSERT INTO table_receipt VALUES(? , ? , ? , ? , ? , ?)",(receipt_id,menu_id,count,price,date,daily_receipt_id))
        self.connection.commit()
        self.connection.close()

    
    def get_max_daily_receipt(self):
        today = JalaliDatetime.now().strftime('%Y/%m/%d')
        #today=1402/10/16
        self.connection= sqlite3.connect(self.__db_name)
        self.cursor=self.connection.cursor()
        self.cursor.execute("SELECT MAX(daily_receipt_id) FROM table_receipt WHERE date = ?", (today,))
        result = self.cursor.fetchall()
        return result
    

    def get_receipt_by_receiptid_menuid(self,receipt_id,menu_id):
        self.connection= sqlite3.connect(self.__db_name)
        self.cursor=self.connection.cursor()
        self.cursor.execute("SELECT * FROM table_receipt WHERE receipt_id=? AND menu_id=?" , (receipt_id,menu_id,))
        result = self.cursor.fetchall()
        return result


    def increase_count(self,receipt_id,menu_id):
        self.connection= sqlite3.connect(self.__db_name)
        self.cursor=self.connection.cursor()
        self.cursor.execute("UPDATE table_receipt SET count=count+1 WHERE receipt_id=? And menu_id=? ",(receipt_id,menu_id,))
        self.connection.commit()
        self.connection.close()


    def get_receipt_by_receiptid(self,receipt_id):
        self.connection= sqlite3.connect(self.__db_name)
        self.cursor=self.connection.cursor()
        self.cursor.execute("SELECT * FROM view_menu_receipt WHERE receipt_id=?",(receipt_id,))
        result = self.cursor.fetchall()
        return result




db=None

if os.path.isfile('restaurant.db')== False:
    db= Database('restaurant.db')
    db.insert(1, 'هات داگ',22000,True)
    db.insert(2, 'برنج',25000,True)
    db.insert(3, 'نوشابه',22000,False)
    db.insert(4, 'آب معدنی',22000,False)
else:
    db= Database('restaurant.db')


