import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ashil333!",
    auth_plugin="mysql_native_password"
)#Open database connection

#prepare a cursor obj using cursor() method
cursor = db.cursor()

#excute SQL query using excute() method
sql="SELECT VERSION()"
cursor.execute(sql)

#fetch a single row using fetchone() method
data = cursor.fetchone()
print("Database version:",data)

#disconnect from server
db.close()