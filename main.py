from db_setup import initialize_database
from authentication import initialize_users, authenticate_user
from access_control import query_data, update_health_record
from integrity_protection import hash_data, verify_data
from confidentiality import encrypt_data, decrypt_data

# Set up a simple key for encryption (for demonstration purposes)
from Crypto.Random import get_random_bytes
encryption_key = get_random_bytes(16)  # 16 bytes long key for AES

def main():
    # Step 1: Initialize the Database and Users
    initialize_database()
    print("Database initialized.")
    initialize_users()
    print("Users initialized.")

    # Step 2: Authenticate the user
    username = input("Enter username to login: ")
    password = input("Enter password to login: ")
    if authenticate_user(username, password):
        print("Authentication successful.")
    else:
        print("Authentication failed.")
        return

    # Step 3: Query data
    user_group = input("Enter user group for querying data (H/R): ")
    data = query_data(user_group)
    print("Data Retrieved:", data)

    # Step 4: Update a health record (optional)
    update_choice = input("Do you want to update a record? (y/n): ")
    if update_choice.lower() == 'y':
        record_id = int(input("Enter record ID to update: "))
        field = input("Enter field to update (e.g., age, weight): ")
        new_value = input("Enter new value: ")
        
        # Convert value to correct data type based on field
        if field in {"age"}:
            new_value = int(new_value)
        elif field in {"weight", "height"}:
            new_value = float(new_value)
        elif field == "gender":
            new_value = bool(int(new_value))  # 0 or 1 for gender
        
        update_health_record(record_id, field, new_value)

    # Step 5: Test encryption and decryption (for demonstration)
    sample_data = "Sensitive Health Data"
    hashed = hash_data(sample_data)
    print("Data Hash:", hashed)
    if verify_data(sample_data, hashed):
        print("Data integrity verified.")

    encrypted_data = encrypt_data(sample_data, encryption_key)
    print("Encrypted Data:", encrypted_data)
    decrypted_data = decrypt_data(encrypted_data, encryption_key)
    print("Decrypted Data:", decrypted_data)

if __name__ == "__main__":
    main()
