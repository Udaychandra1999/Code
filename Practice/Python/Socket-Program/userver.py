import socket

def userver():
    host = socket.gethostname()
    port = 1116

    server_socket = socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM) #type DGRAM represents UDP

    server_socket.bind((host,port))
    data = server_socket.recvfrom(1024)
    data,addr = data
    print(f"from client:{data}")
    data = input("->")
    server_socket.sendto(data.encode(),addr)

    server_socket.close()

if __name__ == "__main__":
    userver()