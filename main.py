from db_setup import initialize_database
from authentication import initialize_users, authenticate_user
from authentication import initialize_users, authenticate_user
from access_control import query_data, add_data
from confidentiality import encrypt_data
from integrity import generate_hash, verify_data_integrity

def main():
    initialize_database()
    initialize_users()

    print("Enter username to login:")
    username = input("Username: ")
    password = input("Password: ")

    if authenticate_user(username, password):
        print("Authentication successful.")
        user_group = input("Enter user group for querying data (H/R): ")
        data = query_data(user_group)
        
        if data:
            for record in data:
                print("Data Retrieved:", record)
            data_hash = generate_hash(str(data))
            print("Data Hash:", data_hash)
            
            if verify_data_integrity(str(data), data_hash):
                print("Data integrity verified.")
            else:
                print("Data integrity check failed.")
            
            sensitive_data = f"{data[0][2]} {data[0][3]}"
            encryption_key = "Sixteen byte key"
            nonce, ciphertext, tag = encrypt_data(sensitive_data, encryption_key)
            print("Encrypted Data:", ciphertext)
        else:
            print("No data found for the user group.")
    else:
        print("Authentication failed. Exiting program.")

if __name__ == "__main__":
    main()
