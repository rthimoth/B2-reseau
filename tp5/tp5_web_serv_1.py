import socket

def start_server(port=13337):
    # Créer un socket pour établir une communication réseau
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Associer le socket à l'adresse du serveur (localhost) et au port spécifié
    server_socket.bind(('localhost', port))

    # Le serveur écoute les connexions entrantes
    server_socket.listen()

    print(f"Serveur démarré, en attente de requêtes sur le port {port}...")

    while True:
        # Accepter une nouvelle connexion
        conn, addr = server_socket.accept()
        with conn:
            print(f"Connecté à {addr}")
            request = conn.recv(1024).decode('utf-8')
            print(f"Requête reçue: \n{request}")

            # Préparer la réponse HTTP
            http_response = "HTTP/1.1 200 OK\nContent-Type: text/html\n\n<h1>Hello, je suis un serveur HTTP</h1>"

            # Envoyer la réponse au client
            conn.sendall(http_response.encode('utf-8'))

if __name__ == "__main__":
    start_server()
