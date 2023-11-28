import socket
import struct

def read_calculation(conn):
    # Lecture des entiers et de l'opérateur
    num1_bytes = conn.recv(4)
    operator_byte = conn.recv(1)
    num2_bytes = conn.recv(4)

    # Déballage des entiers et de l'opérateur
    num1 = struct.unpack('!I', num1_bytes)[0]
    operator = struct.unpack('!c', operator_byte)[0].decode()
    num2 = struct.unpack('!I', num2_bytes)[0]

    return num1, operator, num2

# Configuration initiale du serveur
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('10.1.2.12', 13337))
s.listen(1)
conn, addr = s.accept()

print("Connecté à:", addr)

try:
    # Lecture du calcul
    num1, operator, num2 = read_calculation(conn)

    # Effectuer le calcul
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    else:
        raise ValueError("Opérateur invalide")

    # Envoi du résultat
    conn.send(struct.pack('!I', result))
finally:
    conn.close()
    s.close()
