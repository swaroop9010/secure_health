import mysql.connector
from mysql.connector import errorcode

def initialize_database():
    # Connect to MySQL
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Homesh@99"
    )
    cursor = conn.cursor()

    # Create database and use it
    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS secure_health_db")
        cursor.execute("USE secure_health_db")
        
        # Create tables
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS health_info (
                id INT AUTO_INCREMENT PRIMARY KEY,
                first_name VARCHAR(50),
                last_name VARCHAR(50),
                gender BOOLEAN,
                age INT,
                weight FLOAT,
                height FLOAT,
                health_history TEXT
            )
        """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                username VARCHAR(50) PRIMARY KEY,
                password VARBINARY(60),
                user_group CHAR(1) CHECK (user_group IN ('H', 'R'))
            )
        """)
        
        # Insert sample health data
        cursor.executemany("""
            INSERT INTO health_info (first_name, last_name, gender, age, weight, height, health_history) 
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, [
            ('John', 'Smith', 1, 35, 75.5, 180.5, 'No significant medical history'),
            ('Jane', 'Doe', 0, 28, 62.3, 165.2, 'Mild allergies'),
            ('Alice', 'Brown', 0, 42, 68.0, 170.0, 'Diabetes type 2'),
            ('Bob', 'Johnson', 1, 50, 80.0, 175.0, 'Hypertension'),
            ('Carol', 'Davis', 0, 33, 55.0, 160.0, 'Asthma')
        ])
        
        conn.commit()
        print("Database initialized with sample records.")
        
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        conn.close()
