import socket

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #tcp 

# Bind the socket to the address and port
server_address = ('127.0.0.1', 1234) #localhost
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(5)

print("Server is listening on port 1234...")

while True:
    # Wait for a connection
    print("Waiting for a connection...")
    client_socket, client_address = server_socket.accept()

    try:
        print("Connection established with", client_address)
        
        # Receive data from the client
        data = client_socket.recv(1024) #1MB
        print("Received:", data.decode()) #לפענח את המידע שהלקוח שלח 

        # Send a response back to the client
        response = "Message received successfully!"
        client_socket.sendall(response.encode()) 
        
    finally:
        # Clean up the connection
        client_socket.close()