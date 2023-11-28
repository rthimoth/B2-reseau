import socket
import struct

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('127.0.0.1', 9999))
s.listen(1)
conn, addr = s.accept()

while True:
    try:
        # On reçoit l'entier du client, empaqueté en 4 octets (pour un int)
        data = conn.recv(4)
        if not data:
            break
        number = struct.unpack('!I', data)[0]  # Unpack the bytes to an integer
        print(f"Nombre reçu du client: {number}")

        # Traitement (par exemple, incrémenter le nombre)
        number += 1

        # On renvoie l'entier traité, empaqueté
        conn.send(struct.pack('!I', number))
    except socket.error:
        print("Error Occurred.")
        break

conn.close()
