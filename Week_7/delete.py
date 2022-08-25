import mysql.connector
from mysql.connector import errorcode

# connect to DB
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
    totalprice = input("Enter totalprice of cart to delete ")


    cart_query = ("DELETE FROM cart "
                      "WHERE totalprice = %s")
    cart_data = (totalprice,)
    try:
        cart_cursor = cm_connection.cursor()
        cart_cursor.execute(cart_query, cart_data)
        cm_connection.commit()
        print("Deleted record")
        cart_cursor.close()
    except mysql.connector.Error as err:
        print("\nrecord not deleted")
        print("Error: {}".format(err))
    cm_connection.close()
