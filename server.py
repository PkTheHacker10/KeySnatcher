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
            print("waiting for data..")
            data=conn.recv(BUFFER_SIZE).decode()
            print("data received..")
            if not data:
                print("\nConnection closed\nPress enter to quit.")
                break

            if data:
                #print(f"\n{data}",end="")
                print(data)

            else:
                break

        except TimeoutError:
            continue

    sock.close()

if __name__ == "__main__":
    receive_data()


