import os
from highrise import BaseBot, Highrise
import asyncio

class MyBot(BaseBot):
    async def on_start(self, session_metadata) -> None:
        print("ربات آنلاین شد!")

async def main():
    room_id = os.environ.get("ROOM_ID")
    token = os.environ.get("TOKEN")
    
    bot = MyBot()
    hr = Highrise()
    await hr.connect(room_id, token)
    await hr.run(bot)

if __name__ == "__main__":
    asyncio.run(main())
    
