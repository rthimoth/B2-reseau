import socket
import sys

# On définit la destination de la connexion
host = '10.1.2.12'  # IP du serveur
port = 13337        # Port choisi par le serveur

try:
    # Création de l'objet socket de type TCP (SOCK_STREAM)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connexion au serveur
    s.connect((host, port))
    print(f"Connecté avec succès au serveur {host} sur le port {port}")

    # Demande à l'utilisateur ce qu'il veut envoyer
    message = input("Que veux-tu envoyer au serveur : ")
    s.sendall(message.encode())

    # On reçoit la réponse du serveur
    data = s.recv(1024).decode('utf-8')
    print(f"Le serveur a répondu : {data}")

except Exception as e:
    print(f"Une erreur est survenue: {e}")
    sys.exit(1)

finally:
    # On libère le socket TCP
    s.close()
