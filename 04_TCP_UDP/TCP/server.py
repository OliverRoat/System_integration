import socket

HOST = '127.0.0.1'  # Localhost
PORT = 2222         # Same port as the Node.js server

# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))  # Bind to address and port
server_socket.listen(1)  # Listen for incoming connections

print(f"TCP Server listening on {HOST}:{PORT}")

while True:
    client_socket, client_address = server_socket.accept()  # Accept a client connection
    print(f"Client connected from {client_address}")

    client_socket.sendall(b'Hello from the server')  # Send data to client

    data = client_socket.recv(1024)  # Receive data
    if data:
        print(f"Data received from client: {client_address} - {data.decode()}")
        client_socket.sendall(b'Hello Client')  # Reply to client

    client_socket.close()  # Close connection
    print(f"Client disconnected: {client_address}")
