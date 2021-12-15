import mysql.connector
import requests

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="salvatore"
)

print(mydb)
