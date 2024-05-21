import socket

# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the server's address and port
server_address = ('127.0.0.1', 1234)
client_socket.connect(server_address)

try:
    while True:
        # Get user input
        message = input("Enter message to send (or type 'quit' to exit): ")

        # Check if the user wants to quit
        if message.lower() == 'quit':
            break

        # Send the message to the server
        print("Sending:", message)
        client_socket.sendall(message.encode())

        # Receive the echoed message from the server
        echoed_message = client_socket.recv(1024)
        print("server answer:", echoed_message.decode())

finally:
    # Clean up the connection
    client_socket.close()