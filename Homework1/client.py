import socket
import sys

numbers = ['', '', '']

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    if len(sys.argv) != 4:
        print("Usage: $python client.py <ip_address> <port_number> <host_name>")
        sys.exit(1)

    s.connect((sys.argv[1], int(sys.argv[2])))

    packet = 'GET' + ' ' + sys.argv[3]
    s.sendall(packet.encode('utf-8'))
    data = s.recv(1024).decode('utf-8')
    print('Received:', data)

    # close the connection and terminate the program
    s.close()
    sys.exit(0)

    # while True:
    #     data = s.recv(1024).decode('utf-8')
    #     status = data.split(' ')[0]
    #     data = data[len(status)+1:]
    #
    #     if data and status == 'fibo':
    #         print(data)
    #         numbers[0:1] = data.split(',')
    #         numbers[2] = int(numbers[0]) + int(numbers[1])
    #         packet = str(numbers[1]) + ',' + str(numbers[2])
    #         s.sendall(packet.encode('utf-8'))
    #
    #     if data and status == 'end':
    #         print(data)
    #         print('Connection is closed')
    #         break
    #
    #     if not data:
    #         pass

