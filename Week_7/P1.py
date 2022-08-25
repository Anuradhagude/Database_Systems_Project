import mysql.connector
from mysql.connector import errorcode

# connect to DB
try:
   cm_connection = mysql.connector.connect(
      user="cm_user",
      password="pyuser5134",
      host="127.0.0.1",
      database="classicmodels")

except mysql.connector.Error as err:
   if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
      print("Invalid credentials")
   elif err.errno == errorcode.ER_BAD_DB_ERROR:
      print("Database not found")
   else:
      print("Cannot connect to database:", err)

else:
    employee_last = input("Enter employee last name ")
    column = input("Enter item to update (officeCode, lastName, jobTitle, extension) ")
    prompt = "Enter new value for {} ".format(column)
    value = input(prompt)

    employee_query = ("UPDATE employees "
                      "SET " + column + " =  %s "
                      "WHERE lastName = %s")
    employee_data = (value, employee_last)
    try:
        employee_cursor = cm_connection.cursor()
        employee_cursor.execute(employee_query, employee_data)
        cm_connection.commit()
        print("Updated employee")
        employee_cursor.close()
    except mysql.connector.Error as err:
        print("\nEmployee not updated")
        print("Error: {}".format(err))
    cm_connection.close()
