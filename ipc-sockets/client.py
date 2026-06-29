import socket
import time

# ─── IPC SOCKET CLIENT ────────────────────────────────────
HOST = '127.0.0.1'
PORT = 5000

# Messages to send to the server
MESSAGES = [
    "Hello from the client process!",
    "This is IPC via sockets",
    "Sending message 3 of 3"
]

def start_client():
    # Create the socket and connect to server
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    print(f"[CLIENT] Connected to server at {HOST}:{PORT}\n")

    try:
        for message in MESSAGES:
            # Send message to server
            print(f"[CLIENT] Sending: \"{message}\"")
            client_socket.send(message.encode('utf-8'))

            # Wait for server reply
            reply = client_socket.recv(1024).decode('utf-8')
            print(f"[CLIENT] Server replied: \"{reply}\"\n")

            time.sleep(1)  # pause between messages

    finally:
        client_socket.close()
        print("[CLIENT] Connection closed")

if __name__ == "__main__":
    start_client()