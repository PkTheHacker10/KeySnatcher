# decryptor.py
import sys
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

PASSWORD = b"password"

def decrypt_message(b64_data):
    raw_data = base64.b64decode(b64_data)
    salt = raw_data[:16]
    print(f"salt : {salt}")
    print(f"message : {raw_data[16:]}")
    encrypted_message = raw_data[16:]

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=1200000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(PASSWORD))
    fernet = Fernet(key)
    decrypted = fernet.decrypt(encrypted_message)
    return decrypted.decode()

# Example usage
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: decryptor.py <base64_encrypted_text>")
        sys.exit(1)

    b64_input = sys.argv[1]
    try:
        result = decrypt_message(b64_input)
        print("Decrypted:", result)
    except Exception as e:
        print("Decryption failed:", str(e))
