
import socket

HOST = '127.0.0.1'
PORT = 65431

status = 'start'
numbers = ['', '', '']
hopCount = 20 

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()

    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024).decode('utf-8')
            if data and status == 'start':
                print(data)
                status = 'fibo'
                packet = data + ' ' + data
                conn.sendall(packet.encode('utf-8'))

            elif data and status == 'fibo':
                if hopCount > 0:
                    print(data)
                    numbers[0:1] = data.split(',')
                    numbers[2] = int(numbers[0]) + int(numbers[1])
                    packet = str(numbers[1]) + ',' + str(numbers[2])
                    packet = status + ' ' + packet
                    conn.sendall(packet.encode('utf-8'))

                    hopCount -= 1

                else:
                    status = 'end'
                    packet = 'Last fibo number calculated: ' + str(numbers[2])
                    packet = status + ' ' + packet
                    conn.sendall(packet.encode('utf-8'))

            else:
                pass

            if not data:
                break

