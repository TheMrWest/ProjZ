import projz
import asyncio
import json

c = projz.Client()

async def main():
    r = await c.login_email("teste", "teste2")
    print(r)

asyncio.run(main())
