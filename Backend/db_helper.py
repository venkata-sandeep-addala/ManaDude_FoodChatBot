import mysql.connector
from mysql.connector import Error

global conn

try:
    conn = mysql.connector.connect(
        host='localhost',
        database='pandeyji_eatery',
        user='root',
        password='Lav@2000')

except Error as e:
    print("Error while connecting to MySQL:", e)

def get_order_status(order_id: int) -> str:  # type: ignore
    try:
        if conn.is_connected():
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT status FROM order_tracking WHERE order_id = %s", (order_id,))
            result = cursor.fetchone()
            if result:
                return result['status'] # type: ignore
            return "Order ID not found."
    except Error as e:
        print("Error while fetching order status:", e)
        return "An error occurred while fetching the order status."
    finally:
        if cursor:
            cursor.close()