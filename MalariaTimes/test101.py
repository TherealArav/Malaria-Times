# libraries
import mysql.connector as msc
from subprocess import call

myConnector = msc.connect(host = "localhost",user = "root",password = "MySql1234IsDaBest",database = "data12")  # connect() function
if myConnector.is_connected():  # checking whether communication has been established sucessfully
    print("Python enviorment version connected to MySQL database succefully!")

myCursor = myConnector.cursor()

userInput = input("USERNAME: ")
passInput = input("PASSWORD: ")
myCursor.execute(f"INSERT INTO USERNAMES VALUES('{userInput}','{passInput}');")
myConnector.commit()
myConnector.close()             
call(["python","Malaria.py"])
