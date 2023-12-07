import asyncio
import aiohttp
import aiofiles
import sys

async def get_content(url):
    """ Effectue une requête HTTP GET de manière asynchrone et retourne le contenu de la page. """
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def write_content(content, file):
    """ Écrit le contenu dans un fichier spécifié de manière asynchrone. """
    async with aiofiles.open(file, mode='w', encoding='utf-8') as f:
        await f.write(content)

async def main(url):
    file_path = "web_page1.txt"  # Chemin pour Windows
    content = await get_content(url)
    await write_content(content, file_path)
    print(f"Contenu téléchargé et sauvegardé dans {file_path}")

if __name__ == "__main__":
    url = sys.argv[1]  # Récupère l'URL depuis la ligne de commande
    asyncio.run(main(url))
