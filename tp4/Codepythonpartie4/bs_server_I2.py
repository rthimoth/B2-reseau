import socket

# On choisit une IP et un port où on va écouter
host = '10.1.2.12' # L'adresse IP du serveur
port = 13337       # Le port choisi par le serveur

# Création de la socket TCP/IP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)
print(f"Le serveur écoute sur {host}:{port}")

while True:
    # Acceptation d'une nouvelle connexion
    conn, addr = s.accept()
    print(f"Un client vient de se co et son IP c'est {addr[0]}")

    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break

            # Conversion des données reçues en chaîne de caractères
            message = data.decode()
            print(f"Données reçues du client : {message}")

            # Réponse adaptative selon le message
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
