import socket
import sys
from shared import get_encrypted_timestamp, KEY

def handle_client(sock, key):
    '''Handles a single client interaction for the UDP server.'''
    data, addr = sock.recvfrom(1024) # Receive data from client
    print(f"Connected by {addr}")
    try:
        encrypted_timestamp = get_encrypted_timestamp(key)
        sock.sendto(encrypted_timestamp, addr) # Send encrypted timestamp to client
    finally:
        pass # No connection to close in UDP

def main(port):
    '''Starts the UDP server listening on the given port.'''
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.bind(('', port))
        print(f"UDP Server listening on port {port}")

        while True:
            handle_client(sock, KEY) # Handle clients continuously

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: tpudpserver <port>")
        sys.exit(1)
    
    main(int(sys.argv[1]))
