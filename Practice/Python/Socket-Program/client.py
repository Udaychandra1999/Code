import socket

def clientProgram():
    host = socket.gethostname()
    port = 1111

    """socket connect send/recv"""

    client_socket = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)
    client_socket.connect((host,port))
    
    data = client_socket.recv(1024).decode()

    print(f"From server: {str(data)}")
    data = input("->")
    client_socket.send(data.encode())

    client_socket.close()

if __name__ == "__main__":
    clientProgram()

