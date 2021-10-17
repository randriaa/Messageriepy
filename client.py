################# Coté Client ####################

import socket

Host = "192.168.1.93"
Port = 6390

#Création du socket
socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

socket.connect((Host , Port))

while True: 
    msg = input("->")
    msg = msg.encode('utf-8')
    socket.send(msg)
    
    requete_server = socket.recv(500)
    requete_server = requete_server.decode("utf-8")
    print(requete_server)