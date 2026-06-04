import os
import asyncio
from highrise import BaseBot, Bot

class MyBot(BaseBot):
    async def on_start(self, session_metadata) -> None:
        print("ربات با موفقیت در اتاق مستقر شد!")

async def main():
    # دریافت اطلاعات از محیط
    room_id = os.environ.get("ROOM_ID")
    token = os.environ.get("TOKEN")
    
    # اتصال ربات به صورت مستقیم و بدون واسطه
    bot = MyBot()
    await Bot(bot, room_id, token).run()

if __name__ == "__main__":
    # اجرای ایزوله در حلقه asyncio
    asyncio.run(main())
