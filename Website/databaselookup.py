import sqlite3 

db = sqlite3.connect("dayyip.db") 
cursor = db.cursor() 

cursor.execute("SELECT * FROM uyeler") 
veriler = cursor.fetchall()
print(veriler)