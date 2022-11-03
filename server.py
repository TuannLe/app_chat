import socket
import threading

HOST = '127.0.0.1'
POST = 9090

FORMAT = 'utf-8'


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, POST))

server.listen()

clients = []
nicknames = []

#broadcast
def broadcast(message):
    for client in clients:
        client.send(message)

# handle
def handle(client):
    while True:
        try:
            message = client.recv(1024)
            print(f"{nicknames[clients.index(client)]} says {message}")
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            nicknames.remove(nickname)
            break

# receive
def receive():
    while(True):
        client, address = server.accept()
        print(f"Connect with {str(address)}")

        client.send("NICK".encode(FORMAT))
        nickname = client.recv(1024)

        nicknames.append(nickname)
        clients.append(client)

        print(f"Nickname of the client {nickname}")
        broadcast(f"{nickname} connected to the server!\n".encode(FORMAT))
        client.send("Connected to the server".encode(FORMAT))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print("Server running...")
receive()