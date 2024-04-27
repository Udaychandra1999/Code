import socket

def clientProgram():
    host = socket.gethostname()
    port = 1116

    server_socket = socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)

    data = input("->")
    server_socket.sendto(data.encode(),(host,port))
    data = server_socket.recvfrom(1024)
    print(f"from server:{data}")
    server_socket.close()

if __name__ == "__main__":
    clientProgram()