import socket
import threading


def handle_client(client_socket):
    while True:
        message = client_socket.recv(1024).decode()
        if message.lower().strip() == "bye":
            break
        print("Received from client: " + message)
        response = "Server response: " + message
        client_socket.send(response.encode())
    client_socket.close()


def server_program():
    host = socket.gethostname()
    port = 5000

    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen()

    while True:
        client_socket, address = server_socket.accept()
        print("Connection from: " + str(address))
        threading.Thread(target=handle_client, args=(client_socket,)).start()


if __name__ == "__main__":
    server_program()
