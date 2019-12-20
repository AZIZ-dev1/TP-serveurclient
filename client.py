import socket

hote = "localhost"
port = 12800

connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_avec_serveur.connect((hote, port))
print("Connexion établie avec le serveur sur le port {}".format(port))


num1 = input("Enter first number: ")

num2 = input("Enter second number: ")
op = input("Enter the operation: ")

connexion_avec_serveur.send(num1.encode())
connexion_avec_serveur.send(num2.encode())
connexion_avec_serveur.send(op.encode())
result = connexion_avec_serveur.recv(1024)

print(num1,op,num2,"=",result.decode())







"""
msg_a_envoyer = b""
while msg_a_envoyer != b"fin":
    msg_a_envoyer = input("Enter the first number: ")
    # Peut planter si vous tapez des caractères spéciaux
    msg_a_envoyer = msg_a_envoyer.encode()
    # On envoie le message
    connexion_avec_serveur.send(msg_a_envoyer)
    msg_recu = connexion_avec_serveur.recv(1024)
    print(msg_recu.decode()) # Là encore, peut planter s'il y a des accents
"""
print("Fermeture de la connexion")
connexion_avec_serveur.close()