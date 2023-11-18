import mysql.connector as mys

mydb = mys.connect(
  host="localhost",
  user="root",
  password="root"
)

if mys.is_connected():
    print("aaa")