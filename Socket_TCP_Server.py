import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("0.0.0.0", 1337))
server_socket.listen(10)

while True:
        conn, addr = server_socket.accept()
        conn.send(b"Do you want to play a game?\n")
        received = conn.recv(1024)
        print(received)

server_socket.close()