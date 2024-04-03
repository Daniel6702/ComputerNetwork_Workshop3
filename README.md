# (1) Overall Description of the Implementation
These scripts are designed to demonstrate basic network communication using the socket API in Python. 
The core functionality revolves around sending an encrypted timestamp from the server to the client
and then analyzing it on the client side.

## TCP Implementation
The TCP part includes a server script that listens for incoming connections on a 
specified port and a client script that connects to this server. The server sends an encrypted timestamp 
to the connected client, and the client decrypts and analyzes this timestamp.

## UDP Implementation
The UDP part also includes a server and a client script. The UDP server listens for 
incoming datagrams and responds to them without establishing a persistent connection. The client
sends a request and receives the encrypted timestamp from the server, which it then decrypts and analyzes.

In the TCP client/server implementation, the server listens for connections (sock.listen()), 
and upon receiving a connection request (sock.accept()), it establishes a reliable communication channel. 
The client initiates the connection (s.connect()) before any data is sent.
TCP is more reliable and ensures data integrity and order but is slower due to its overhead
- Connection-Oriented
- Flow Control and Congestion Control
- Ordered Delivery

In the UDP client/server implementation, the server waits for incoming datagrams 
(sock.recvfrom()) and responds without establishing a persistent connection. 
The client sends a datagram (s.sendto()) without prior connection setup.
This makes the UDP implementation simpler but less reliable compared to TCP.
- Connectionless
- no mechanism for retransmission, ordering, or data integrity (Reliability)
- UDP has lower latency

# (2) Socket API Usage in the Implementation
The socket API is a way to enable inter-process communication and is widely used for network programming.

### Creating a Socket:
TCP: socket.socket(socket.AF_INET, socket.SOCK_STREAM) creates a TCP socket.
UDP: socket.socket(socket.AF_INET, socket.SOCK_DGRAM) creates a UDP socket.

### Server Setup:
TCP: The server uses 'bind' to bind the socket to an address and 'listen' to listen for incoming connections. 'accept' is used to accept a connection.
UDP: The server binds the socket to an address but does not need to listen or accept connections since UDP is connectionless.

### Client Connection:
TCP: The client uses 'connect' to establish a connection with the server.
UDP: The client does not need to establish a connection and directly sends data using sendto.

### Data Transmission:
TCP: Data is sent and received using 'sendall' and 'recv' methods on the connected sockets.
UDP: Data is sent and received using 'sendto' and 'recvfrom' methods.

### Closing the Socket:
In both TCP and UDP implementations, sockets are closed after their respective operations are completed to free up resources. This is done using the 'close' method or by using a 'with' statement which automatically takes care of closing the socket.
