import hashlib

def generate_hash(data):
    """
    Generate a SHA-256 hash for the given data.
    """
    hash_object = hashlib.sha256(data.encode('utf-8'))
    return hash_object.hexdigest()

def verify_data_integrity(data, hash_value):
    """
    Verify the integrity of the data by comparing hashes.
    """
    return generate_hash(data) == hash_value
