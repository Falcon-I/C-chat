import time, socket, sys
try:
    print("type 'stop_chat_server' to exit")
    time.sleep(1)
    soc = socket.socket()
    host_name = socket.gethostname()
    ip = socket.gethostbyname(host_name)
    port = 1234
    soc.bind((host_name, port))
    name = input("Enter your name :")
    soc.listen(100)
    print('Waiting for connection from client.....')
    connection, addr = soc.accept()
    print("Received connection from client")
    client_name = connection.recv(1024)
    client_name = client_name.decode()
    print(client_name + ' has connected.')
    connection.send(name.encode())
    while True:
        message = input('                                                                               You' + '>> ')
        if message == 'stop_chat_server':
            message2 = 'Bye........(SIGNAL LOST)'
            connection.send(message2.encode())
            break
        connection.send(message.encode())
        message = connection.recv(1024)
        message = message.decode()
        print(client_name, '>>', message)
except:
    print("Client is offline")
