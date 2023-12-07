import socket

def main():
    host = '127.0.0.1'  # Adresse du serveur
    port = 8888  # Le même port que votre serveur

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(b"Hello")  # Envoi d'un message au serveur
        data = s.recv(1024)  # Réception de la réponse du serveur

    print(f"Reçu du serveur : {data.decode()}")

if __name__ == "__main__":
    main()
