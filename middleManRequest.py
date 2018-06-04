import os
import socket
import sys
import json
def iter (first, last):
    data_file = open(os.path.dirname(__file__) + "MOCK_DATA.json")
    temp = json.load(data_file)
    for x in xrange(0, len(temp)):
        if temp(x)[2] == first:
            if temp(x)[3] == last:
                return True
    return False

def checkRequest(first, last): #order matters
# Create a TCP/IP socket
    sock = socket.socket(   socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('0.0.0.0', 5000)
    print >>sys.stderr, 'starting up on %s port %s' % server_address
    sock.bind(server_address)
    sock.listen(1)

    print >> sys.stderr, "type exit to stop"

    while True:
        # Wait for a connection
        print >>sys.stderr, 'waiting for a connection'
        connection, client_address = sock.accept()
        try:
            print >> sys.stderr, 'connection from', client_address

            # Receive the data in small chunks and retransmit it
            while True:
                data = connection.recv(63333)
                print >> sys.stderr, data

                iter(first,last)







                ask = raw_input()
                connection.sendall(ask)
                if data == "exit":
                    print >> sys.stderr, 'no more data from', client_address
                    break
            break
        finally:
            # Clean up the connection
            connection.close()