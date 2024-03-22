import socket
import sys
from shared import get_encrypted_timestamp, KEY

def handle_client(sock, key):
    '''Handles a single client connection for the TCP server.'''
    conn, addr = sock.accept() # Accept a new connection
    print(f"Connected by {addr}")
    try:
        encrypted_timestamp = get_encrypted_timestamp(key)
        conn.sendall(encrypted_timestamp) # Send encrypted timestamp to client
    finally:
        conn.close() # Ensure connection is closed after handling

def main(port):
    '''Starts the TCP server listening on the given port.'''
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind(('', port))
        sock.listen()
        print(f"TCP Server listening on port {port}")

        while True:
            handle_client(sock, KEY) # Handle clients continuously

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python tptcpserver.py <port>")
        sys.exit(1)
    
    main(int(sys.argv[1]))
