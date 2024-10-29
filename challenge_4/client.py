import socket
import threading
from time import sleep

# create Socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect and enter username
username = f'[{input("enter username：")}]'
client_socket.connect(('localhost', 12345))
client_socket.send(f'{username} joins'.encode('utf-8'))

#receive message from other client
def receiving_message():
    #start sending message
    threading.Thread(target = sending_message).start()
    while True:
        received = client_socket.recv(1024).decode('utf-8')
        if not received:
            break
        print(f'{received}')

def sending_message():
    while True:
        # 获取消息get message
        sleep(0.2)
        message = f'[{username}]:{input("enter text: ")}'
        if message.lower() == f'{username}:exit':  # type exit to exit
            client_socket.send(f'{username} disconnected'.encode('utf-8'))
            break
        # send
        client_socket.send(message.encode('utf-8'))

receiving_message()
client_socket.close()
