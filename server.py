import tkinter as tk
import tkinter.scrolledtext as st
import time, socket, sys, os

soc = socket.socket()
host_name = socket.gethostname()
ip = socket.gethostbyname(host_name)
port = 1234
soc.bind((host_name, port))
name = "Chaitu"
soc.listen(100)
connection, addr = soc.accept()
client_name = connection.recv(1024)
fyclient_name = client_name.decode()

def start():
    try:
        message_show.insert(tk.INSERT, fyclient_name + " has connected.\n")
    except:
        message_show.insert(tk.INSERT, "Clients are offline.\n")

def sends():
    try:
        my_message = message_box.get()
        connection.send(my_message.encode())
        message_show.insert(tk.INSERT, name + " : " + my_message + ".\n")
    except:
        message_show.insert(tk.INSERT, "Signal lost. Can't send your message.\n")



def receive():
    try:
        client_message = connection.recv(1024)
        fyclient_message = client_message.decode()
        message_show.insert(tk.INSERT, fyclient_name + " : " + fyclient_message + ".\n")
    except:
        message_show.insert(tk.INSERT, "Signal lost.....\n")


root = tk.Tk()
root.title("C-chat")
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
root.geometry("%dx%d" % (screenwidth, screenheight))
root['background'] = '#856ff8'
message_show = st.ScrolledText(width = 80,height = 30)
message_show.grid(column = 0, padx = 300, pady = 100)
message_box = tk.Entry()
message_box.place(x=300, y=650, width=600, height=40)
start = tk.Button(text="Start Server", width=10, height=2, command=start)
start.place(x=0, y=0)
send = tk.Button(text="Send", width=10, height=2, command=sends)
send.place(x=910, y=650)
receive = tk.Button(text="Receive", width=10, height=2, command=receive)
receive.place(x=1290, y=0)



root.mainloop()
