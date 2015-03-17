import socket
import sys
import time

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address given on the command line
#server_name = sys.argv[1]
#port = sys.argv[2]
server_name = "localhost"
port = "9999"
server_address = (server_name, int(port))
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)
sock.listen(1)

while True:
    print >>sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept()
    try:
        print >>sys.stderr, 'client connected:', client_address
        portfolio="portfolio 1 A:20 B:30\n"
        portfolio1="portfolio 2 A:30 B:10\n"
        portfolio2="portfolio 3 A:10 B:20\n"
        price="price A:10 B:34\n"
        while True:
            connection.sendall(portfolio)
            connection.sendall(portfolio1)
            connection.sendall(portfolio2)
            connection.sendall(price)
            time.sleep(2)
    finally:
        connection.close()
