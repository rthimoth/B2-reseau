import socket
import argparse
import sys

# Configuration de l'analyseur d'arguments
parser = argparse.ArgumentParser()
parser.add_argument('-p', '--port', type=int, default=13337, 
                    help="Le port TCP sur lequel le serveur doit écouter."
                    'Run server'
        '-p ou --port  ensuite donne le port pour écouter dessus'
                       'les ports dispo sont tous les ports inférieur a 65535'  
                       'les ports privilégiés sont les ports de 0 a 1024'                 
)

args = parser.parse_args()

# Vérification de la validité du port
if args.port < 0 or args.port > 65535:
    print("ERROR: Le port spécifié n'est pas un port possible (de 0 à 65535).")
    sys.exit(1)
if args.port >= 0 and args.port <= 1024:
    print("ERROR: Le port spécifié est un port privilégié. Spécifiez un port au-dessus de 1024.")
    sys.exit(2)

# Utilisation du port spécifié ou du port par défaut
port = args.port

# Début de la configuration du serveur
host = '10.1.2.12'  # Écoute sur toutes les interfaces

# Reste du code serveur...
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)
print(f"Le serveur écoute sur {host}:{port}")

while True:
    conn, addr = s.accept()
    print(f"Un client vient de se co et son IP c'est {addr[0]}")

    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break

            message = data.decode()
            print(f"Données reçues du client : {message}")

            if "meo" in message:
                response = "Meo à toi confrère."
            elif "waf" in message:
                response = "ptdr t ki"
            else:
                response = "Mes respects humble humain."

            conn.sendall(response.encode())

    except socket.error:
        print("Une erreur de socket est survenue.")
        break

    finally:
        conn.close()
