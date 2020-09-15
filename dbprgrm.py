import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ashil333!",
    auth_plugin="mysql_native_password",
    database="luminarpython"
)

print(db)
cursor=db.cursor()

try:
    query="SELECT FIRST_NAME FROM EMPLOYEE WHERE INCOME > 1000"
    cursor.execute(query)
    result=cursor.fetchall()

    for x in result:
        print(x)
except Exception as e:
    print(e.args)
finally:
    db.close