import time, socket, threading
import tkinter.scrolledtext as st
import tkinter as tk

server = '192.168.29.137'
soc = socket.socket()
shost = socket.gethostname()
ip = socket.gethostbyname(shost)
server_host = server
name = input("your name :")
port = 1234
time.sleep(1)
soc.connect((server_host, port))
print("Conneteced")
soc.send(name.encode())
server_name = "Chaitu"



def sends():
    try:
        my_message = message_box.get()
        soc.send(my_message.encode())
        message_show.insert(tk.INSERT, name + " : " + my_message + ".\n")
    except:
        message_show.insert(tk.INSERT, "Signal lost. Can't send your message.\n")




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
send = tk.Button(text="Send", width=10, height=2, command=sends)
send.place(x=910, y=650)




def rec():
    try:
        while True:
            client_message = soc.recv(1024)
            fyclient_message = client_message.decode()
            message_show.insert(tk.INSERT, server_name + " : " + fyclient_message + ".\n")
    except:
        message_show.insert(tk.INSERT, "Signal lost.....\n")


try:
    threading.Thread(target=rec).start()

except:
    message_show.insert(tk.INSERT, "Signal lost.....\n")



root.mainloop()
