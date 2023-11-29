import socket

# Configuration du socket serveur
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('10.1.2.12', 13337))
server_socket.listen()

print("Le serveur HTTP écoute sur le port 8080...")

while True:
    # Accepter une connexion entrante
    client_connection, client_address = server_socket.accept()
    request = client_connection.recv(1024).decode('utf-8')
    print(f"Requête reçue: {request}")

    # Analyse de la requête HTTP
    headers = request.split('\n')
    if headers[0].startswith('GET / '):
        # Réponse HTTP
        http_response = "HTTP/1.0 200 OK\n\n<h1>Hello je suis un serveur HTTP</h1>"
        client_connection.sendall(http_response.encode('utf-8'))
    else:
        # Réponse pour les autres cas (non gérés)
        http_response = "HTTP/1.0 404 Not Found\n\n<h1>404 Not Found</h1>"
        client_connection.sendall(http_response.encode('utf-8'))

    # Fermer la connexion
    client_connection.close()

# Attention: ce code ne gère pas correctement toutes les situations et est fourni à des fins éducatives uniquement.
