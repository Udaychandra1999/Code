import socket

""" socket bind listen accept send/recv"""

def serverProgram():
    host = socket.gethostname()
    port = 1111

    server_socket = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)
    server_socket.bind((host,port))

    server_socket.listen(2)

    conn,addr = server_socket.accept()

    print(f"Connected : {str(addr)}")
    data = input("->")
    conn.send(data.encode())

    data = conn.recv(1024).decode()
    print(f"Msg from client: {str(data)}")

    conn.close()

if __name__ == "__main__":
    serverProgram()