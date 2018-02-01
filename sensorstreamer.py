import socket

BUFFER_SIZE = 1024
PORT = 3400

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((socket.gethostname(), PORT))
print "Listening..."
serversocket.listen(5)

while True:
    (clientsocket, address) = serversocket.accept()
    # print(address)
    while True:
        data = clientsocket.recv(BUFFER_SIZE)
        if not data:
            break
        print data
    clientsocket.close()
