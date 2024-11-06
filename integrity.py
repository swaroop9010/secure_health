import hashlib

def generate_hash(data):
    hash_object = hashlib.sha256(data.encode('utf-8'))
    return hash_object.hexdigest()

def verify_data_integrity(data, hash_value):
    return generate_hash(data) == hash_value
