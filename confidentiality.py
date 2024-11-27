from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

def encrypt_data(data, key):
    """
    Encrypt sensitive data using AES encryption.
    """
    cipher = AES.new(key.encode('utf-8'), AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(data.encode('utf-8'))
    return nonce, ciphertext, tag

def decrypt_data(nonce, ciphertext, tag, key):
    """
    Decrypt encrypted data using AES decryption.
    """
    cipher = AES.new(key.encode('utf-8'), AES.MODE_EAX, nonce=nonce)
    data = cipher.decrypt_and_verify(ciphertext, tag)
    return data.decode('utf-8')
