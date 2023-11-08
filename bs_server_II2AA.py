import socket
import argparse
import sys
import logging
from datetime import datetime, timedelta

# Configuration du logger
logger = logging.getLogger("bs_server")
logger.setLevel(logging.INFO)

# Formatter pour afficher le niveau de log, le timestamp et le message
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

# Handler pour écrire dans le fichier de log
file_handler = logging.FileHandler('/var/log/bs_server/bs_server.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# Handler pour écrire dans la console avec des couleurs
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

# Configuration de l'analyseur d'arguments
parser = argparse.ArgumentParser()
parser.add_argument('-p', '--port', type=int, default=13337, help="Le port TCP sur lequel le serveur doit écouter.")
args = parser.parse_args()

# Vérification de la validité du port
if args.port < 0 or args.port > 65535:
    logger.error("Le port spécifié n'est pas un port possible (de 0 à 65535).")
    sys.exit(1)
if args.port >= 0 and args.port <= 1024:
    logger.error("Le port spécifié est un port privilégié. Spécifiez un port au-dessus de 1024.")
    sys.exit(2)

# Utilisation du port spécifié ou du port par défaut
port = args.port
host = '10.1.2.12'  # Écoute sur toutes les interfaces

# Lancement du serveur
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)
logger.info(f"Le serveur tourne sur {host}:{port}")

last_client_time = datetime.now()

while True:
    try:
        conn, addr = s.accept()
        logger.info(f"Un client {addr[0]} s'est connecté.")
        last_client_time = datetime.now()

        while True:
            data = conn.recv(1024)
            if not data:
                break
            message = data.decode()
            logger.info(f"Le client {addr[0]} a envoyé {message}")
            response = "Réponse par défaut du serveur."
            if "meo" in message:
                response = "Meo à toi confrère."
            elif "waf" in message:
                response = "ptdr t ki"
            else:
                response = "Mes respects humble humain."
            conn.sendall(response.encode())
            logger.info(f"Réponse envoyée au client {addr[0]} : {response}")

    except socket.error as e:
        logger.error(f"Une erreur de socket est survenue : {e}")

    finally:
        conn.close()
    
    # Vérification de la connexion client
    if datetime.now() - last_client_time > timedelta(minutes=1):
        logger.warning("Aucun client depuis plus de une minute.")
        last_client_time = datetime.now()
