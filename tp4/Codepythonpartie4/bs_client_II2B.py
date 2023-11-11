import logging
import socket
import sys
import re

# Configuration du logger
logger = logging.getLogger("bs_client")
logger.setLevel(logging.INFO)

# Chemin vers le fichier de log du client
log_file_path = "/var/log/bs_clients/bs_clients.log"

# Formatter
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

# FileHandler
file_handler = logging.FileHandler(log_file_path)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

class ErrorFilter(logging.Filter):
    def filter(self, record):
        return record.levelname == 'ERROR'

console_handler = logging.StreamHandler()
console_handler.addFilter(ErrorFilter())
error_formatter = logging.Formatter('\033[91mERROR: %(message)s\033[0m')  # ANSI escape codes for red text
console_handler.setFormatter(error_formatter)
logger.addHandler(console_handler)

# On définit la destination de la connexion
host = '10.1.2.12'  # IP du serveur
port = 13337        # Port choisi par le serveur

try:
    # Création de l'objet socket de type TCP (SOCK_STREAM)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connexion au serveur
    s.connect((host, port))
    logger.info(f"Connecté avec succès au serveur {host} sur le port {port}")

    # Demande à l'utilisateur ce qu'il veut envoyer
    message = input("Que veux-tu envoyer au serveur : ")

    # Vérification que l'input est une string
    if not isinstance(message, str):
        raise TypeError("Le message doit être une chaîne de caractères.")

    # Vérification que la string contient "waf" ou "meo"
    if not re.search(r"waf|meo", message):
        raise ValueError("Le message doit contenir le mot 'waf' ou 'meo'.")

    # Envoi du message après les vérifications
    s.sendall(message.encode())
    logger.info(f"Message envoyé au serveur {host} : {message}")

    # On reçoit la réponse du serveur
    data = s.recv(1024).decode('utf-8')
    logger.info(f"Réponse reçue du serveur {host} : {data}")
    

except (TypeError, ValueError) as e:
    logger.error(f"Erreur lors de la saisie : {e}")
    sys.exit(1)

except Exception as e:  # Pour les autres exceptions éventuelles
    logger.error(f"Impossible de se connecter au serveur {host} sur le port {port}.")
    sys.exit(1)

finally:
    # On libère le socket TCP
    s.close()