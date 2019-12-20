import socket
from op import add
from op import sub
from op import mul
from op import div

hote = ''
port = 12800

connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_principale.bind((hote, port))
connexion_principale.listen(5)
print("Le serveur écoute à présent sur le port {}".format(port))

connexion_avec_client, infos_connexion = connexion_principale.accept()

num1 = float(connexion_avec_client.recv(1))

num2 = float(connexion_avec_client.recv(1))

op = connexion_avec_client.recv(1).decode()

if op=="+":
    result=add(num1,num2)
if op=='-':
    result=sub(num1,num2)
if op=='*':
    result=mul(num1,num2)
if op=='/':
    result=div(num1,num2)
#if op=='%':
    #result=add(num1,num2)
connexion_avec_client.send(str(result).encode())

"""
msg_recu = b""
while msg_recu != b"fin":
    # L'instruction ci-dessous peut lever une exception si le message
    # Réceptionné comporte des accents
    msg_recu2 = connexion_avec_client.recv(1024)
    print(2*msg_recu2.decode())
    connexion_avec_client.send(b"5 / 5")
"""


print("Fermeture de la connexion")
connexion_avec_client.close()
connexion_principale.close()
