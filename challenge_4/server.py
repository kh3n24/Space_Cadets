import socket
import threading

#build server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 12345))
server.listen(5)
print('wait for client to connect...')

clients = []
history = []

def accept_connection():
    while True:
        client_socket, client_address = server.accept()
        print(f'{client_address} connected')
        # send history to client
        if history:
            for item in history:
                client_socket.send(f'{item}\n'.encode('utf-8'))
        clients.append(client_socket)
        threading.Thread(target = accept_message, args = (client_socket,)).start()

def accept_message(target_socket):
    while True:
        message = target_socket.recv(1024).decode('utf-8')
        if not message:
            break
        history.append(message)
        #send message to all client
        for client in clients:
            client.send(message.encode('utf-8'))
            print(clients)
            print('message sent')
        print(message)
    clients.remove(target_socket)
    target_socket.close()

accept_connection()
server.close()