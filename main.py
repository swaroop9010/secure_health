from db_setup import initialize_database
from authentication import initialize_users, authenticate_user
from access_control import query_data, add_data, verify_query_completeness
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
        print(f"User Group: {user_group}")

        # Query data based on the user group (H or R)
        data, original_hash = query_data(user_group)

        if data:
            print("Data Retrieved:", data)
            
            # Verify data integrity
            if verify_data_integrity(str(data), original_hash):
                print("Data integrity verified.")
            else:
                print("Data integrity verification failed.")
            
            # Simulate data modification for completeness check
            modified_data = data[:-1] if len(data) > 1 else data  # Avoid errors if only one record exists
            if verify_query_completeness(modified_data, original_hash):
                print("Query completeness verified.")
            else:
                print("Query completeness check failed: Data was modified.")
            
            # Encrypt sensitive data (e.g., gender and age)
            sensitive_data = f"{data[0][2]} {data[0][3]}"  # Example: gender and age
            encryption_key = "SixteenByteKey!!"  # Ensure 16 bytes for AES
            nonce, ciphertext, tag = encrypt_data(sensitive_data, encryption_key)
            print("Encrypted Data:", ciphertext)

            # Decrypt and verify encryption
            decrypted_data = decrypt_data(nonce, ciphertext, tag, encryption_key)
            print("Decrypted Data:", decrypted_data)
        else:
            print("No data found for the user group.")
    else:
        print("Authentication failed. Exiting program.")

if __name__ == "__main__":
    main()
