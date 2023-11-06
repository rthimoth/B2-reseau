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

    # Envoi de data bidon
    s.sendall(b'Meooooo !')

    # On reçoit 1024 bytes qui contiennent peut-être une réponse du serveur
    data = s.recv(1024)

    # Affichage de la réponse reçue du serveur
    print(f"Le serveur a répondu {repr(data)}")

except Exception as e:  # Cette ligne doit être au même niveau d'indentation que 'try'
    print(f"Une erreur est survenue: {e}")
    sys.exit(1)  # Se termine avec un code d'erreur car une exception s'est produite

finally:  # Cette ligne doit être au même niveau d'indentation que 'try' et 'except'
    # On libère le socket TCP
    s.close()
    sys.exit(0)  # Se termine avec un code de succès