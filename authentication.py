import mysql.connector
import bcrypt

def initialize_users():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Homesh@99",
        database="secure_health_db"
    )
    cursor = conn.cursor()
    
    users = [
        {"username": "root", "password": "Homesh@99", "user_group": "H"},
        {"username": "swaroop", "password": "password1", "user_group": "R"},
        {"username": "yamini", "password": "password2", "user_group": "R"}
    ]
    
    for user in users:
        hashed_password = bcrypt.hashpw(user["password"].encode(), bcrypt.gensalt())
        cursor.execute(
            "INSERT INTO users (username, password, user_group) VALUES (%s, %s, %s) "
            "ON DUPLICATE KEY UPDATE password = VALUES(password), user_group = VALUES(user_group)",
            (user["username"], hashed_password, user["user_group"])
        )
    conn.commit()
    cursor.close()
    conn.close()

def authenticate_user(username, password):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Homesh@99",
        database="secure_health_db"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM users WHERE username = %s", (username,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    
    if result is None:
        return False  # User not found

    # Convert the stored password from bytearray to bytes if necessary
    stored_password = bytes(result[0])

    return bcrypt.checkpw(password.encode(), stored_password)

