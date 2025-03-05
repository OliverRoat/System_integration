import socket

HOST = '127.0.0.1'
PORT = 2222

# Create a TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))  # Connect to server

print(f"Connected to server {HOST}:{PORT}")

client_socket.sendall(b'Hello Server')  # Send data to server

data = client_socket.recv(1024)  # Receive data from server
print(f"Data received from server: {data.decode()}")

client_socket.close()  # Close connection
print("Connection closed")
