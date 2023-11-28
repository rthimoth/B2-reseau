import socket
import struct

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 9999))

# On envoie le nombre 100000 empaqueté en 4 octets
s.send(struct.pack('!I', 100000))

# On reçoit la réponse du serveur, un entier empaqueté
data = s.recv(4)
number = struct.unpack('!I', data)[0]  # Unpack the bytes to an integer
print(f"Réponse du serveur: {number}")

s.close()