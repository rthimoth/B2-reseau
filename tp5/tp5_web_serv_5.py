import socket
import os
import mimetypes
import logging

# Configuration du logging
log_file_path = 'www/var/log/tp5/server.log'
os.makedirs(os.path.dirname(log_file_path), exist_ok=True)
logging.basicConfig(filename=log_file_path, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def serve_file(filepath, client_address):
    if not os.path.exists(filepath):
        logging.warning(f"File not found: {filepath} requested by {client_address}")
        return "HTTP/1.1 404 NOT FOUND\n\nFile Not Found".encode()

    # Déterminer le type MIME du fichier
    mime_type, _ = mimetypes.guess_type(filepath)
    if mime_type is None:
        mime_type = 'application/octet-stream'

    # Lire et envoyer le fichier en morceaux
    with open(filepath, 'rb') as file:
        content = file.read(1024)
        header = f"HTTP/1.1 200 OK\nContent-Type: {mime_type}\n\n".encode()
        while content:
            conn.sendall(header + content)
            content = file.read(1024)
            header = b""
        logging.info(f"File served: {filepath} to {client_address}")

def start_server(port=8080):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', port))
    server_socket.listen(5)

    print(f"Serveur démarré, écoute sur le port {port}...")

    while True:
        conn, addr = server_socket.accept()
        with conn:
            request = conn.recv(1024).decode('utf-8')
            uri = request.split(' ')[1]
            if uri == '/':
                uri = '/index.html'
            filepath = 'www' + uri
            serve_file(filepath, addr)

if __name__ == "__main__":
    start_server()
