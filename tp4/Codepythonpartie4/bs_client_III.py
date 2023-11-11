import logging
import socket
import sys
import re

# Configuration du logger
logger = logging.getLogger("bs_client")
logger.setLevel(logging.INFO)

# Formatter
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

# FileHandler
file_handler = logging.FileHandler("/var/log/bs_clients/bs_clients.log")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# StreamHandler pour la sortie console avec couleur pour les erreurs
class CustomStreamHandler(logging.StreamHandler):
    def __init__(self):
        super().__init__()

    def emit(self, record):
        # Définir les codes de couleur ANSI pour les erreurs
        red_color = '\033[91m'
        reset_color = '\033[0m'
        original_formatter = self.formatter

        # Si le niveau de log est ERROR, ajouter les codes de couleur
        if record.levelno == logging.ERROR:
            self.formatter = logging.Formatter(f"{red_color}{original_formatter._fmt}{reset_color}", datefmt='%Y-%m-%d %H:%M:%S')

        # Appeler la méthode emit originale
        super().emit(record)

        # Réinitialiser le formateur à son état d'origine
        self.formatter = original_formatter

stream_handler = CustomStreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

# On définit la destination de la connexion
host = '10.1.2.12'  # IP du serveur
port = 13337        # Port choisi par le serveur

def validate_expression(expression):
    # Valide les composants individuels de l'expression
    for part in re.split(r'\s*[\+\-\*\/]\s*', expression):
        if part:
            number = int(part)
            if number < -100000 or number > 100000:
                return False
    return True

try:
    # Création de l'objet socket de type TCP (SOCK_STREAM)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connexion au serveur
    s.connect((host, port))
    logger.info(f"Connecté avec succès au serveur {host} sur le port {port}")

    while True:
        # Demande à l'utilisateur de saisir une opération arithmétique
        operation = input("Entrez une opération arithmétique ou 'exit' pour quitter: ")
        if operation.lower() == 'exit':
            break

        # Vérification de la validité de l'opération à l'aide d'une expression régulière
        if not re.match(r'^[-+]?[0-9]+(\s*[-+*/]\s*[-+]?[0-9]+)*$', operation):
            logger.error("Opération invalide.")
            continue
        
        # Vérification supplémentaire pour les limites des nombres
        if not validate_expression(operation):
            logger.error("Les nombres doivent être compris entre -100000 et +100000.")
            continue

        # Envoi de l'opération au serveur
        s.sendall(operation.encode())
        logger.info(f"Opération envoyée: {operation}")

        # Réception de la réponse du serveur
        response = s.recv(1024).decode('utf-8')
        logger.info(f"Réponse reçue: {response}")

except Exception as e:
    logger.error(f"Une erreur est survenue: {e}")
    sys.exit(1)

finally:
    # On libère le socket TCP
    s.close()
    logger.info("Connexion fermée.")
