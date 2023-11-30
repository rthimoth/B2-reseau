import requests

def send_get_request(url):
    try:
        response = requests.get(url)
        print(f"Statut de la réponse : {response.status_code}")
        print("Contenu de la réponse :")
        print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la requête : {e}")

if __name__ == "__main__":
    url = input("Entrez l'URL pour envoyer une requête GET (par exemple, http://localhost:8080) : ")
    send_get_request(url)
