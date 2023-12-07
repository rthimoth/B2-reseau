import asyncio

CLIENTS = {}

async def broadcast_message(message, exclude_writer=None):
    for client in CLIENTS.values():
        if client["w"] is not exclude_writer:
            try:
                client["w"].write(message.encode())
                await client["w"].drain()
            except ConnectionError:
                # Gérer l'erreur de connexion si nécessaire
                pass

async def handle_client(reader, writer):
    addr = writer.get_extra_info('peername')
    first_data = await reader.read(1024)
    pseudo = first_data.decode().split("|")[1].strip() if first_data.startswith(b"Hello|") else "Inconnu"
    CLIENTS[addr] = {"r": reader, "w": writer, "pseudo": pseudo}
    await broadcast_message(f"Annonce : {pseudo} a rejoint la chatroom")

    while True:
        data = await reader.read(1024)
        if not data:
            message = f"Annonce : {CLIENTS[addr]['pseudo']} a quitté la chatroom"
            del CLIENTS[addr]
            await broadcast_message(message, exclude_writer=writer)
            break
        message = f"{CLIENTS[addr]['pseudo']} a dit : {data.decode()}"
        await broadcast_message(message, exclude_writer=writer)

    writer.close()

async def main():
    server = await asyncio.start_server(handle_client, '127.0.0.1', 8888)
    addr = server.sockets[0].getsockname()
    print(f"Serving on {addr}")

    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())
