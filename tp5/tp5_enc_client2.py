import socket
import struct
import re

def send_calculation(sock, num1, operator, num2):
    # Encodage des entiers et de l'opérateur
    num1_bytes = struct.pack('!I', num1)  # Format '!I' pour un entier non signé en réseau (big-endian)
    operator_bytes = struct.pack('!c', operator.encode())  # Format '!c' pour un caractère
    num2_bytes = struct.pack('!I', num2)

    # Envoi de chaque partie avec un en-tête de taille
    sock.send(num1_bytes)
    sock.send(operator_bytes)
    sock.send(num2_bytes)

# Création d'un socket et connexion au serveur
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('10.1.2.12', 13337))

# Récupération et validation de l'entrée utilisateur
calculation = input("Entrez le calcul (format: 'nombre opérateur nombre'): ")
match = re.match(r'(\d+)\s*([\+\-\*])\s*(\d+)', calculation)
while not match:
    print("Format invalide, veuillez entrer une expression comme '2 + 2'.")
    calculation = input("Entrez le calcul: ")
    match = re.match(r'(\d+)\s*([\+\-\*])\s*(\d+)', calculation)

num1, operator, num2 = match.groups()

# Envoi du calcul
send_calculation(s, int(num1), operator, int(num2))

# Réception et affichage du résultat
result_data = s.recv(1024)
print(result_data.decode())

# Fermeture de la connexion
s.close()
