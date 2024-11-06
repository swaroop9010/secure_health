import bcrypt
import mysql.connector

# Initialize predefined users
def initialize_users():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Homesh@99",
        database="secure_health_db"
    )
    cursor = conn.cursor()

    # Define three specific users
    users = [
        {"username": "user1", "password": "user1@99", "user_group": "H"},
        {"username": "user2", "password": "user2@99", "user_group": "H"},
        {"username": "user3", "password": "user3@99", "user_group": "H"}
    ]

    # Register each user if they don't already exist
    for user in users:
        cursor.execute("SELECT * FROM users WHERE username = %s", (user["username"],))
        if not cursor.fetchone():
            hashed_password = bcrypt.hashpw(user["password"].encode('utf-8'), bcrypt.gensalt())
            cursor.execute("INSERT INTO users (username, password, user_group) VALUES (%s, %s, %s)",
                           (user["username"], hashed_password, user["user_group"]))

    conn.commit()
    conn.close()

# Authenticate user
def authenticate_user(username, password):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Homesh@99",
        database="secure_health_db"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM users WHERE username = %s", (username,))
    stored_password = cursor.fetchone()
    conn.close()

    if stored_password:
        # Convert stored_password[0] to bytes if it's a bytearray
        return bcrypt.checkpw(password.encode('utf-8'), bytes(stored_password[0]))
    else:
        return False
