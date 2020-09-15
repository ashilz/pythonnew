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

query="INSERT INTO EMPLOYEE(FIRST_NAME,LAST_NAME,AGE,SEX,INCOME) VALUES('ASHIL','ANTONY',26,'M',30000)"
try:
    cursor.execute(query)
    db.commit()
except Exception as e:
    db.rollback()
    print(e.args)
finally:
    db.close()
