import mysql.connector
from mysql.connector import errorcode
import random

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
    cart_query = "SELECT * FROM Cart"
    cart_cursor = cm_connection.cursor()
    cart_cursor.execute(cart_query)
    for row in cart_cursor.fetchall():
        print("The Total Price for Cart ID {} is {} on {}".format(row[0], row[2], row[1]))
    cart_cursor.close()

    id = input("Enter Cart ID: ")
    date = input("Enter Date: ")
    totalprice = input("Enter Total Price: ")

    insert_cart = ("INSERT INTO cart"
                  "(id, date, totalprice)"
                  "VALUES (%s,%s,%s)")

    cart_a = (id, date, totalprice)
    try:
        cart_cursor = cm_connection.cursor()
        cart_cursor.execute(insert_cart, cart_a)
        cm_connection.commit()
        print("Added New Record into Cart")
        cart_cursor.close()
    except mysql.connector.Error as err:
        print("\nNew Record not added")
        print("Error: {}".format(err))
    print("SUCCESS")
    cm_connection.close()

