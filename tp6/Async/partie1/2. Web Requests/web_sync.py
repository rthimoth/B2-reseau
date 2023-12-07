import requests
import sys

def get_content(url):
    response = requests.get(url)
    return response.text

def write_content(content, file):
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    url = sys.argv[1] 
    content = get_content(url)
    file_path = "web_page.txt"
    write_content(content, file_path)
    print(f"Contenu téléchargé et sauvegardé dans {file_path}")