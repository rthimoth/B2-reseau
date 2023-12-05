import asyncio

async def f1():
    for i in range(5):
        print(i)
        await asyncio.sleep(1)

async def f2():
    for i in range(5):
        print(i + 10)
        await asyncio.sleep(1)

async def main():
    tasks = [f1(), f2()]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
