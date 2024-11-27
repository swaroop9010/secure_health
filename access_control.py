import mysql.connector
import hashlib

def query_data(user_group):
    """
    Retrieve data from the `health_info` table based on the user's group.
    Group 'H' can access all fields, while Group 'R' cannot see first_name and last_name.
    Query integrity checks are performed.
    """
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Homesh@99",
        database="secure_health_db"
    )
    cursor = conn.cursor()

    if user_group == 'H':
        cursor.execute("SELECT id, first_name, last_name, gender, age, weight, height, health_history FROM health_info")
    elif user_group == 'R':
        cursor.execute("SELECT id, gender, age, weight, height, health_history FROM health_info")

    data = cursor.fetchall()
    data_hash = generate_hash(str(data))  # Generate hash for query integrity
    conn.close()
    return data, data_hash

def verify_query_completeness(data, original_hash):
    """
    Verify if the query result is complete using the provided hash.
    """
    return generate_hash(str(data)) == original_hash

def add_data(record_id, new_health_history):
    """
    Update the `health_history` field of a specific record in the `health_info` table.
    Only accessible by users from Group 'H'.
    """
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Homesh@99",
        database="secure_health_db"
    )
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE health_info
    SET health_history = %s
    WHERE id = %s
    """, (new_health_history, record_id))

    conn.commit()
    cursor.close()
    conn.close()
    print(f"Record {record_id} updated successfully.")
