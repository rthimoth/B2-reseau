import socket
import argparse
import sys
import logging
from datetime import datetime, timedelta
import re

# Configuration du logger
logger = logging.getLogger("bs_server")
logger.setLevel(logging.INFO)

# Formatter pour afficher le niveau de log, le timestamp et le message
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

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

def safe_eval(expr):
    """ Évalue une expression arithmétique en toute sécurité. """
    # Autoriser uniquement les opérations arithmétiques de base avec des nombres entiers
    if not re.match(r'^[\d\+\-\*\/\(\) ]+$', expr):
        raise ValueError("Opération non autorisée.")
    # Évaluer l'expression
    return eval(expr, {'__builtins__': None}, {})

try:
    while True:
        try:
            conn, addr = s.accept()
            logger.info(f"Un client {addr[0]} s'est connecté.")
            last_client_time = datetime.now()

            while True:
                data = conn.recv(1024)
                if not data:
                    break
                try:
                    expression = data.decode().strip()
                    result = safe_eval(expression)
                    response = f"Le résultat de '{expression}' est {result}."
                except (ValueError, SyntaxError):
                    response = "Erreur : Opération non autorisée ou invalide."
                except Exception as e:
                    response = f"Erreur : {e}"
                
                conn.sendall(response.encode())
                logger.info(f"Calcul reçu : {expression}, réponse envoyée : {response}")

        except socket.error as e:
            logger.error(f"Une erreur de socket est survenue : {e}")

        finally:
            conn.close()

        # Vérification de la connexion client
        if datetime.now() - last_client_time > timedelta(minutes=1):
            logger.warning("Aucun client depuis plus de une minute.")
            last_client_time = datetime.now()

except KeyboardInterrupt:
    logger.info("Arrêt du serveur initié par l'utilisateur.")
finally:
    s.close()
