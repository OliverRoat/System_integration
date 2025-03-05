import socket

HOST = '127.0.0.1'
PORT = 2222

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message = b'Hello Server'

# Send data to server
client_socket.sendto(message, (HOST, PORT))
print("Packet sent successfully")

# Receive response from server
data, server_address = client_socket.recvfrom(1024)
print(f"Message from server: {data.decode()}")

client_socket.close()  # Close socket
