import asyncio
import aioconsole

async def send_message(writer):
    while True:
        message = await aioconsole.ainput("Message: ")
        writer.write(message.encode())
        await writer.drain()

async def receive_message(reader):
    while True:
        data = await reader.read(1024)
        if not data:
            print("Le serveur s'est déconnecté.")
            break
        print(f"Reçu: {data.decode()}")

async def main():
    reader, writer = await asyncio.open_connection('127.0.0.1', 8888)

    pseudo = input("Entrez votre pseudo: ")
    writer.write(f"Hello|{pseudo}".encode())

    send_task = asyncio.create_task(send_message(writer))
    receive_task = asyncio.create_task(receive_message(reader))

    await asyncio.gather(send_task, receive_task)

if __name__ == '__main__':
    asyncio.run(main())
