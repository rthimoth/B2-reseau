import asyncio
import websockets
import redis.asyncio as redis

# Connexion au serveur Redis
redis_client = redis.Redis(host="10.1.2.12", port=6379)

async def broadcast_message(message, exclude=None):
    clients = await redis_client.keys('*')  # Récupérer tous les clients
    for client_key in clients:
        if client_key.decode() != exclude:
            try:
                # Simuler l'envoi d'un message (remplacer par une fonction d'envoi réelle)
                print(f"Envoi à {client_key.decode()}: {message}")
            except Exception as e:
                print(f"Erreur lors de l'envoi: {e}")

async def handle_client(websocket, path):
    addr = websocket.remote_address
    pseudo = await websocket.recv()
    pseudo = pseudo.split("|")[1].strip() if pseudo.startswith("Hello|") else "Inconnu"

    # Enregistrer le client dans Redis
    await redis_client.set(addr[0], pseudo)
    
    await broadcast_message(f"Annonce : {pseudo} a rejoint la chatroom", exclude=addr[0])

    try:
        async for message in websocket:
            broadcast_msg = f"{pseudo} a dit : {message}"
            await broadcast_message(broadcast_msg, exclude=addr[0])
    except websockets.exceptions.ConnectionClosed:
        pass

    # Supprimer le client de Redis lorsqu'il se déconnecte
    await redis_client.delete(addr[0])
    await broadcast_message(f"Annonce : {pseudo} a quitté la chatroom")

async def main():
    async with websockets.serve(handle_client, '127.0.0.1', 8888):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())