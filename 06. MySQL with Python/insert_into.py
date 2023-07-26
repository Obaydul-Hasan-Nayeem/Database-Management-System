import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "password",
    database = "mydatabase"
)

mycursor = mydb.cursor()

# insert data
sql_command =   """
                INSERT INTO student(roll, first_name, last_name)
                VALUES(1, "Obaydul Hasan", "Nayeem");
                """

mycursor.execute(sql_command)
mydb.commit()