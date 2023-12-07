import asyncio

CLIENTS = {}

async def handle_client(reader, writer):
    addr = writer.get_extra_info('peername')
    CLIENTS[addr] = {'r': reader, 'w': writer}

    while True:
        data = await reader.read(1024)
        if not data:
            del CLIENTS[addr]
            break

        message = data.decode()
        forward_message = f"{addr[0]}:{addr[1]} a dit: {message}"
        print(forward_message)

        # Envoyer le message à tous les clients sauf à l'expéditeur
        for client_addr, client in CLIENTS.items():
            if client_addr != addr:
                try:
                    client['w'].write(forward_message.encode())
                    await client['w'].drain()
                except ConnectionError:
                    # Gérer l'erreur de connexion si nécessaire
                    pass

    writer.close()

async def main():
    server = await asyncio.start_server(handle_client, '127.0.0.1', 8888)
    addr = server.sockets[0].getsockname()
    print(f"Serving on {addr}")

    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())
