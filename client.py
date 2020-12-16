import time, socket, sys
server = input("server's IP :")
time.sleep(1)
soc = socket.socket()
shost = socket.gethostname()
ip = socket.gethostbyname(shost)
server_host = server
name = input("your name :")
port = 1234
print('Trying to connect to the server: {}, ({})'.format(server_host, port))
time.sleep(1)
soc.connect((server_host, port))
print("Connected...")
soc.send(name.encode())
server_name = soc.recv(1024)
server_name = server_name.decode()
print('{} has joined...'.format(server_name))
print("Enter 'stop_chat_server' to exit.")
while True:
    message = soc.recv(1024)
    message = message.decode()
    print(server_name, ">", message)
    message = input('                                                                     you' + "> ")
    soc.send(message.encode())
    if message == "stop_chat_server":
        message1 = "bye........(SIGNAL LOST)"
        soc.send(message1.encode())
        break
