import socket

HOST=''
PORT=1234
BUFFER_SIZE = 1234

sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind((HOST,PORT))
sock.listen()
conn,addr=sock.accept()

def receive_data():
    while True:
        try:
            data=conn.recv(BUFFER_SIZE).decode()
            if not data:
                print("\nConnection closed")
                break

            if data:
                print(data)

            else:
                break

        except TimeoutError:
            continue

    sock.close()

if __name__ == "__main__":
    receive_data()


