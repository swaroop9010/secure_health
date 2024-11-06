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
