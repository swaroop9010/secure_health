import mysql.connector

def query_data(user_group):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Homesh@99",
        database="secure_health_db"
    )
    cursor = conn.cursor()

    if user_group == "H":
        cursor.execute("SELECT * FROM health_info")
    else:
        cursor.execute("SELECT age, gender, weight, height, health_history FROM health_info")
    
    data = cursor.fetchall()
    conn.close()
    return data

def update_health_record(record_id, field, new_value):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Homesh@99",
        database="secure_health_db"
    )
    cursor = conn.cursor()

    # Ensure only allowed fields are updated
    allowed_fields = {"first_name", "last_name", "gender", "age", "weight", "height", "health_history"}
    if field in allowed_fields:
        cursor.execute(f"UPDATE health_info SET {field} = %s WHERE id = %s", (new_value, record_id))
        conn.commit()
        print(f"Record {record_id} updated successfully.")
    else:
        print("Invalid field specified.")
    
    conn.close()
