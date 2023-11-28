import socket

def read_message(conn):
    # Lecture de l'en-tête pour la taille du message
    header = conn.recv(2)
    message_size = int.from_bytes(header, byteorder='big')

    # Lecture du message basé sur la taille
    message = conn.recv(message_size).decode()

    # Lecture de la séquence de fin (ici '\x00')
    end_seq = conn.recv(1)
    if end_seq != b'\x00':
        raise ValueError("Séquence de fin de message incorrecte.")
    
    return message

# Configuration initiale
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('10.1.2.12', 13337))
s.listen(1)
conn, addr = s.accept()

print("Connecté à:", addr)

try:
    # Lecture et réponse au message initial 'Hello'
    hello_message = read_message(conn)
    print(f"Reçu : {hello_message}")
    conn.send(b'Hello')

    # Lecture du calcul
    calculation = read_message(conn)
    print(f"Calcul reçu : {calculation}")

    # Evaluation du calcul et envoi du résultat
    try:
        result = str(eval(calculation))  # Utiliser 'eval' est risqué (voir note ci-dessous)
        conn.send(result.encode())
    except Exception as e:
        error_msg = f"Erreur : {e}"
        conn.send(error_msg.encode())
finally:
    conn.close()
    s.close()
