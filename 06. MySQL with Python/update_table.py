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
                    UPDATE student
                    SET first_name = "Tanvir", last_name = "Ahmed"
                    WHERE roll = 1;
                """

mycursor.execute(sql_command)
mydb.commit()