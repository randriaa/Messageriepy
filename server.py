################# Coté Serveur ####################

import socket

Host = "192.168.1.93"
Port = 6390

#Création du socket
socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

socket.bind((Host,Port))
socket.listen(1)

#Le script s'arrete jusqu'a une connexion
client, ip = socket.accept()
print("Le client d'adresse ip" , ip , "est connecté")


while True: 
    requete_client = client.recv(500)
    requete_client = requete_client.decode('utf-8')
    print(requete_client)
    if not requete_client : #Si on perd la connexion
        print("CLOSE")
        break
    msg = input("->")
    msg = msg.encode("utf-8")
    client.send(msg)
    
client.close()
socket.close()
