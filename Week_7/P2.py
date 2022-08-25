import mysql.connector
from mysql.connector import errorcode

try:
   cm_connection = mysql.connector.connect(
      user="cs509",
      password="cs509",
      host="127.0.0.1",
      database="nation")

except mysql.connector.Error as err:
   if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
      print("Invalid credentials")
   elif err.errno == errorcode.ER_BAD_DB_ERROR:
      print("Database not found")
   else:
      print("Cannot connect to database:", err)

else:
   # Execute database operations...
   my_cursor = cm_connection.cursor()
   # Build the ‘SELECT’ command to select two columns from a table in your database.
   # I will use firstname and lastname in my Player table.
   cart_query = ("SELECT * FROM Cart")

   my_cursor.execute(cart_query)

   # Display results
   for row in my_cursor.fetchall():
      print("The Total Price for Cart ID {} is {} on {}".format(row[0], row[2]))

   my_cursor.close()
   cm_connection.close()
