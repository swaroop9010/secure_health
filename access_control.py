import mysql.connector
import mysql.connector
def query_data(user_group):
    """
    Retrieve data from the `health_info` table based on the user's group.
    Group 'H' can access all fields, while Group 'R' cannot see first_name and last_name.
    """
    conn = mysql.connector.connect(
        host="localhost",
        user="root",  # Replace with your MySQL username
        password="Homesh@99",  # Replace with your MySQL password
        database="secure_health_db"
    )
    cursor = conn.cursor()

    if user_group == 'H':
        # Group H can access all fields
        cursor.execute("SELECT id, first_name, last_name, gender, age, weight, height, health_history FROM health_info")
    elif user_group == 'R':
        # Group R cannot access first_name and last_name
        cursor.execute("SELECT id, gender, age, weight, height, health_history FROM health_info")

    data = cursor.fetchall()
    conn.close()
    return data

def add_data(record_id, new_health_history):
    """
    Update the `health_history` field of a specific record in the `health_info` table.
    Only accessible by users from Group 'H'.
    """
    conn = mysql.connector.connect(
        host="localhost",
        user="root",  # Replace with your MySQL username
        password="Homesh@99",  # Replace with your MySQL password
        database="secure_health_db"
    )
    cursor = conn.cursor()

    # Update the health history for a specific record by record_id
    cursor.execute("""
    UPDATE health_info
    SET health_history = %s
    WHERE id = %s
    """, (new_health_history, record_id))

    conn.commit()
    cursor.close()
    conn.close()
    print(f"Record {record_id} updated successfully.")
    
def update_data(user_group, record_id, updates):
    if user_group != 'H':
        print("Permission denied: Only Group H users can update data.")
        return False

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="YourPassword",
        database="secure_health_db"
    )
    cursor = conn.cursor()

    # Construct the update query dynamically based on fields provided in `updates`
    set_clause = ", ".join([f"{column} = %s" for column in updates.keys()])
    values = list(updates.values()) + [record_id]

    update_query = f"UPDATE health_info SET {set_clause} WHERE id = %s"
    
    try:
        cursor.execute(update_query, values)
        conn.commit()
        print("Record updated successfully.")
        return True
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return False
    finally:
        cursor.close()
        conn.close()