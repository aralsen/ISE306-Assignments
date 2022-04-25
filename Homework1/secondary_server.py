import socket
import sys

# Create a TCP/IP socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    if len(sys.argv) != 3:
        print("Usage: $python secondary_server.py <port_number> <addresses_file_name>")
        sys.exit(1)

    # Read in file
    lines = []
    with open(sys.argv[2], 'r') as f:
        lines = f.readlines()

    # Split out and drop empty rows
    strip_list = [line.replace('\n', '').split(' ') for line in lines if line != '\n']

    d = dict()
    for strip in strip_list:
        d[strip[0]] = strip[1]

    # Bind the socket to the port
    server_address = ('127.0.0.2', int(sys.argv[1]))
    print('starting up on {} port {}'.format(*server_address))
    sock.bind(server_address)

    # Listen for incoming connections
    sock.listen(1)
    while True:
        # Wait for a connection
        print('waiting for a connection')
        connection, client_address = sock.accept()

        with connection:
            print('connection from', client_address)

            # Receive the data in small chunks and retransmit it
            while True:
                data = connection.recv(1024).decode('utf-8')
                # print('received {!r}'.format(data))
                if data:
                    data_split = data.split(' ')
                    if data_split[0] == 'GET':
                        if data_split[1] in d.keys():
                            # print("Sending {}".format(d[data_split[1]]))
                            message = 'FOUND' + ' ' + data_split[1] + ' ' + d[data_split[1]]
                            connection.sendall(message.encode('utf-8'))
                        else:
                            # print("Sending secondary dns server ip {} {} {}".format(data, sys.argv[2], sys.argv[3]))
                            message = 'ERROR' + ' ' + data_split[1]
                            connection.sendall(message.encode('utf-8'))
                else:
                    pass

                if not data:
                    break
