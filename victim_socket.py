#!/usr/bin/python3
#victim_socket
import subprocess
import socket

subprocess.run(["figlet","victim_socket"])

#if __name__ == "__main__":
victim_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    hacker_IP = "10.0.0.50"
    hacker_port = 8008
    hacker_address = (hacker_IP, hacker_port)
    victim_socket.connect(hacker_address)
    data = victim_socket.recv(1024)
    print(data.decode())
    victim_socket.close()




######### Automaticaly Created Script /##########
