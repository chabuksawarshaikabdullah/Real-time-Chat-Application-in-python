import socket
import threading

# Function to handle receiving messages
def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(message)
        except Exception as e:
            print(f"An error occurred: {e}")
            break

# Function to handle sending messages
def send_messages(client_socket):
    while True:
        message = input()
        client_socket.send(message.encode('utf-8'))

def main():
    host = '127.0.0.1'
    port = 55555

    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the address
    server_socket.bind((host, port))

    # Listen for incoming connections
    server_socket.listen()

    print("Server is listening for incoming connections...")

    # Accept incoming connection
    client_socket, client_address = server_socket.accept()
    print(f"Connection established with {client_address}")

    # Create two threads for sending and receiving messages simultaneously
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    send_thread = threading.Thread(target=send_messages, args=(client_socket,))

    # Start both threads
    receive_thread.start()
    send_thread.start()

if __name__ == "__main__":
    main()

