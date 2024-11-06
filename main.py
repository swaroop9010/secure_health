from db_setup import initialize_database
from authentication import initialize_users, authenticate_user
from access_control import query_data, add_data, update_data
from confidentiality import encrypt_data, decrypt_data
from integrity import generate_hash, verify_data_integrity

def main():
    # Initialize the database and users
    initialize_database()
    initialize_users()

    print("Enter username to login:")
    username = input("Username: ")
    password = input("Password: ")

    # Authenticate the user and get user group
    user_group = authenticate_user(username, password)

    if user_group:
        print("Authentication successful.")
        
        # Option to update records if user is in Group H
        if user_group == 'H':
            update_choice = input("Do you want to update a record? (y/n): ").strip().lower()
            if update_choice == 'y':
                record_id = int(input("Enter the record ID to update: "))
                column = input("Enter the column to update (first_name, last_name, etc.): ")
                new_value = input(f"Enter new value for {column}: ")
                
                # Update the record in the database
                success = update_data(user_group, record_id, {column: new_value})
                if success:
                    print("Record updated successfully.")
                else:
                    print("Failed to update the record.")
        
        # Query data based on the user group (H or R)
        user_query_group = input("Enter user group for querying data (H/R): ").upper()
        data = query_data(user_query_group)
        
        if data:
            for record in data:
                print("Data Retrieved:", record)
            
            # Generate hash for data integrity verification
            data_hash = generate_hash(str(data))
            print("Data Hash:", data_hash)
            
            # Verify data integrity
            if verify_data_integrity(str(data), data_hash):
                print("Data integrity verified.")
            else:
                print("Data integrity check failed.")
            
            # Encrypt sensitive data (e.g., gender and age)
            sensitive_data = f"{data[0][2]} {data[0][3]}"  # Sample sensitive fields: gender and age
            encryption_key = "Sixteen byte key"  # Ensure 16 bytes for AES
            nonce, ciphertext, tag = encrypt_data(sensitive_data, encryption_key)
            print("Encrypted Data:", ciphertext)

            # Optionally, decrypt the data to verify encryption and decryption process
            decrypted_data = decrypt_data(nonce, ciphertext, tag, encryption_key)
            print("Decrypted Data:", decrypted_data)
        else:
            print("No data found for the user group.")
    else:
        print("Authentication failed. Exiting program.")

if __name__ == "__main__":
    main()
