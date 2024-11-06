import mysql.connector
import random

def initialize_database():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",  # Replace with your MySQL username
        password="Homesh@99",  # Replace with your MySQL password
        database="secure_health_db"  # Replace with your database name
    )
    cursor = conn.cursor()

    # Create `users` table for authentication if it doesn't exist
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(50) UNIQUE,
        password VARBINARY(255),
        user_group ENUM('H', 'R') NOT NULL
    );
    """)

    # Create `health_info` table if it doesn't exist
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
    );
    """)

    # Insert 100 random meaningful records into `health_info`
    first_names = [
        'John', 'Jane', 'Michael', 'Emily', 'James', 'Olivia', 'William', 'Sophia', 
        'Henry', 'Isabella', 'Alexander', 'Mia', 'Daniel', 'Charlotte', 'Matthew', 
        'Amelia', 'David', 'Harper', 'Joseph', 'Evelyn', 'Andrew', 'Abigail', 
        'Joshua', 'Ella', 'Samuel', 'Avery', 'Jack', 'Scarlett', 'Ryan', 'Grace', 
        'Ethan', 'Luna', 'Noah', 'Zoey', 'Benjamin', 'Hannah', 'Lucas', 'Victoria', 
        'Liam', 'Nora', 'Oliver', 'Chloe', 'Sebastian', 'Penelope', 'Jackson', 'Riley'
    ]
    last_names = [
        'Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Martinez', 
        'Lopez', 'Wilson', 'Anderson', 'Thomas', 'Taylor', 'Moore', 'Jackson', 
        'Martin', 'Lee', 'Perez', 'Thompson', 'White', 'Harris', 'Sanchez', 
        'Clark', 'Ramirez', 'Lewis', 'Robinson', 'Walker', 'Young', 'Allen', 
        'King', 'Wright', 'Scott', 'Torres', 'Nguyen', 'Hill', 'Flores', 'Green', 
        'Adams', 'Nelson', 'Baker', 'Hall', 'Rivera', 'Campbell', 'Mitchell', 
        'Carter', 'Roberts', 'Gomez', 'Phillips', 'Evans'
    ]
    health_histories = [
        'No significant medical history', 'History of asthma', 'Allergic to penicillin', 
        'History of high blood pressure', 'Diabetic', 'History of migraines', 
        'No known allergies', 'Smoker', 'Non-smoker', 'History of cancer', 
        'History of surgery', 'Frequent traveler', 'Regular exercise', 'High cholesterol', 
        'Vegetarian', 'Pregnant', 'History of anemia', 'History of depression'
    ]

    for _ in range(100):
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        gender = random.choice([True, False])
        age = random.randint(20, 80)
        weight = round(random.uniform(50.0, 100.0), 2)
        height = round(random.uniform(150.0, 200.0), 2)
        health_history = random.choice(health_histories)

        cursor.execute("""
            INSERT INTO health_info (first_name, last_name, gender, age, weight, height, health_history)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (first_name, last_name, gender, age, weight, height, health_history))

    conn.commit()
    conn.close()
    print("Database initialized with 100 random records.")
