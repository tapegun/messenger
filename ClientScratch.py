import socket
import sys
from multiprocessing import Pool

# Create a TCP/IP socket

def makeSocket(ip):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = ('10.3.19.184', 5000)
    print >>sys.stderr, 'connecting to %s port %s' % server_address
    print >> sys.stderr, "type exit to stop"
    sock.connect(server_address)
    print >> sys.stderr, "your socket: " + sock.getsockname()
    sock.connect(server_address)
    print >> sys.stderr, "connected"

    while True:
        message = raw_input()
        # Send data
        sock.sendall(message)
        # Look for the response
        data = sock.recv(63333)
        print >> sys.stderr, data
        if data == "exit":
            print >> sys.stderr, 'closing socket'
            sock.close()
# thing = raw_input("make a socket?(y/n): ")
# thing_1 = raw_input("what is the ip?: ")
# if thing == "y":
#     makeSocket(thing_1)
