import asyncio

async def handle_client(reader, writer):
    while True:
        data = await reader.read(1024)
        if data:
            message = data.decode()
            addr = writer.get_extra_info('peername')
            print(f"Message reçu de {addr[0]}:{addr[1]} : {message}")
        else:
            break

async def main():
    server = await asyncio.start_server(handle_client, '127.0.0.1', 8888)
    addr = server.sockets[0].getsockname()
    print(f"Serving on {addr}")

    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())
