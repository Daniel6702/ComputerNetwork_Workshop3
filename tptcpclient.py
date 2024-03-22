import socket
import sys
from shared import analyze_received_timestamp, KEY

def main(server_host, port):
    '''Connects to the TCP server and retrieves the server time.'''
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((server_host, port)) # Connect to the server
        data = s.recv(4) # Receive the encrypted timestamp (4 bytes)

        if data:
            # Analyze the received timestamp for clock skew, server, and client time
            clock_skew, server_time, client_time = analyze_received_timestamp(data, KEY)
            print(f"Server Time: {server_time}")
            print(f"Client Time: {client_time}")
            print(f"Clock Skew: {clock_skew} seconds")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: tptcpclient <serverhost> <port>")
        sys.exit(1)

    main(sys.argv[1], int(sys.argv[2]))
