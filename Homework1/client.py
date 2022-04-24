
import socket
import sys

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65431        # The port used by the server

numbers = ['', '', '']

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    if len(sys.argv) != 3:
        print("Usage: $python client.py <ip_address> <port_number> <host_name>")
        sys.exit(1)

    s.connect((HOST, PORT))

    packet = 'python.org'
    s.sendall(packet.encode('utf-8'))
    data = s.recv(1024).decode('utf-8')
    print('Received:', data)

    packet = 'ninova.itu.edu.tr'
    s.sendall(packet.encode('utf-8'))
    data = s.recv(1024).decode('utf-8')
    print('Received:', data)

    packet = 'youtube.com'
    s.sendall(packet.encode('utf-8'))
    data = s.recv(1024).decode('utf-8')
    print('Received:', data)

    packet = 'bbf.itu.edu.tr'
    s.sendall(packet.encode('utf-8'))
    data = s.recv(1024).decode('utf-8')
    print('Received:', data)

    packet = 'test'
    s.sendall(packet.encode('utf-8'))
    data = s.recv(1024).decode('utf-8')
    print('Received:', data)

    while True:
        data = s.recv(1024).decode('utf-8')
        status = data.split(' ')[0]
        data = data[len(status)+1:]

        if data and status == 'fibo':
            print(data)
            numbers[0:1] = data.split(',')
            numbers[2] = int(numbers[0]) + int(numbers[1])
            packet = str(numbers[1]) + ',' + str(numbers[2])
            s.sendall(packet.encode('utf-8'))

        if data and status == 'end':
            print(data)
            print('Connection is closed')
            break

        if not data:
            pass

