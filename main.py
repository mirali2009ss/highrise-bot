import os
import asyncio
from highrise import BaseBot, Highrise

class MyBot(BaseBot):
    async def on_start(self, session_metadata) -> None:
        print("ربات با موفقیت در اتاق مستقر شد!")

async def main():
    # Railway متغیرها را از بخش Variables می‌خواند
    room_id = os.environ.get("ROOM_ID")
    token = os.environ.get("TOKEN")
    
    bot = MyBot()
    hr = Highrise()
    await hr.connect(room_id, token)
    await hr.run(bot)

if __name__ == "__main__":
    asyncio.run(main())
