#!/usr/bin/python3
import subprocess
import socket

subprocess.run(["figlet", "Hacker_socket"])

if __name__ == "__main__":
    hacker_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    IP = "10.0.0.50"
    Port = 8008
    socket_address = (IP, Port)
    hacker_socket.bind(socket_address)
    hacker_socket.listen(5)
    print("listening for incoming connection requests")
    hacker_socket, client_address = hacker_socket.accept()
    message = "Message from hacker"
    message_bytes = message.encode()
    hacker_socket.send(message_bytes)
    print("Message sent")
    hacker_socket.close()




######### Automaticaly Created Script /##########
