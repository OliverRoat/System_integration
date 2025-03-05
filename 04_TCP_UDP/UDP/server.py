import socket

HOST = '127.0.0.1'  # Localhost
PORT = 2222         # Same port as the Node.js server

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((HOST, PORT))  # Bind to address and port

print(f"UDP Server listening on {HOST}:{PORT}")

while True:
    data, client_address = server_socket.recvfrom(1024)  # Receive data
    print(f"Message from {client_address[0]}:{client_address[1]} - {data.decode()}")

    response = b'Message received'
    server_socket.sendto(response, client_address)  # Send response
    print("Response sent successfully")
