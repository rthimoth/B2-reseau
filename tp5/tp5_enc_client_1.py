import socket
import re 

def create_header_and_message(msg):
    # Calcul de la taille du message et création de l'en-tête (2 octets pour la taille)
    header = len(msg).to_bytes(2, byteorder='big')
    # Concaténation de l'en-tête, du message et de la séquence de fin
    full_message = header + msg.encode() + b'\x00'  # '\x00' est un exemple de séquence de fin
    return full_message

# Configuration initiale
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('10.1.2.12', 13337))

# Envoi du message initial 'Hello'
s.send(create_header_and_message('Hello'))

# Attente de la réponse initiale du serveur
data = s.recv(1024)
print(data.decode())

# Récupération et envoi du calcul
msg = input("Calcul à envoyer (opérations autorisées: +, -, *): ")
while not re.match(r'^\d+[\+\-\*]\d+$', msg):  # Validation simple de l'expression
    print("Format invalide. Veuillez entrer une expression correcte.")
    msg = input("Calcul à envoyer: ")

s.send(create_header_and_message(msg))

# Réception et affichage du résultat
result_data = s.recv(1024)
print(result_data.decode())

s.close()
