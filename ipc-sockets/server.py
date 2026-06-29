import socket
import datetime

# ─── IPC SOCKET SERVER ────────────────────────────────────
HOST = '127.0.0.1'
PORT = 5000

def start_server():
    # Create the socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)

    print(f"[SERVER] IPC Socket Server started on {HOST}:{PORT}")
    print(f"[SERVER] Waiting for client connection...\n")

    while True:
        # Accept incoming client connection
        client_socket, client_address = server_socket.accept()
        print(f"[SERVER] Client connected from {client_address}")

        try:
            while True:
                # Receive message from client
                data = client_socket.recv(1024).decode('utf-8')
                if not data:
                    break

                timestamp = datetime.datetime.now().strftime("%H:%M:%S")
                print(f"[SERVER] [{timestamp}] Received: \"{data}\"")

                # Process and send reply back
                reply = f"Server received your message: '{data}' at {timestamp}"
                client_socket.send(reply.encode('utf-8'))
                print(f"[SERVER] Reply sent to client\n")

        except ConnectionResetError:
            print(f"[SERVER] Client disconnected")
        finally:
            client_socket.close()

if __name__ == "__main__":
    start_server()