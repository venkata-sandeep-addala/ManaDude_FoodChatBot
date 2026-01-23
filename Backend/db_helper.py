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
            
def get_next_order_id() -> int: # type: ignore
    try:
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute("SELECT MAX(order_id) FROM order_tracking")
            result = cursor.fetchone()
            if result and result[0]: # type: ignore
                return result[0] + 1 # type: ignore
            return 1
    except Error as e:
        print("Error while fetching next order ID:", e)
        return 1
    finally:
        if cursor:
            cursor.close()

def insert_order_item(food_item: str, quantity: int, order_id: int) -> int: # type: ignore
    try:
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.callproc('insert_order_item', (food_item, quantity, order_id))
            conn.commit()
            return 1
    except Error as e:
        print("Error while inserting order item:", e)
        return -1
    finally:
        if cursor:
            cursor.close()
            
            
def insert_order_tracking(order_id: int, status: str) -> None:
    try:
        if conn.is_connected():
            cursor = conn.cursor()
            insert_query = "INSERT INTO order_tracking (order_id, status) VALUES (%s, %s)"
            cursor.execute(insert_query, (order_id, status))
            conn.commit()
    except Error as e:
        print("Error while inserting order tracking:", e)
    finally:
        if cursor:
            cursor.close()
            
def get_total_order_price(order_id: int) -> float: # type: ignore
    try:
        if conn.is_connected():
            cursor = conn.cursor()
            query = f"SELECT get_total_order_price({order_id})"
            cursor.execute(query)
            result = cursor.fetchone()
            if result:
                return result[0] # type: ignore
            return 0.0
    except Error as e:
        print("Error while fetching total order price:", e)
        return 0.0
    finally:
        if cursor:
            cursor.close()