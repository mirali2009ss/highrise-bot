import os
import asyncio
from highrise import BaseBot
from highrise import __main__ as highrise_main
import sys

# کلاس اصلی ربات تو
class MyBot(BaseBot):
    async def on_start(self, session_metadata) -> None:
        print("ربات با موفقیت در اتاق مستقر شد!")

# تابع اجرای ربات بدون استفاده از تابعِ پردردسرِ main()
async def run_bot():
    room_id = os.environ.get("ROOM_ID")
    token = os.environ.get("TOKEN")
    
    # استفاده از متدِ سطح پایین‌تر برای اتصال که آرگومانِ اضافه‌ای نمی‌خواهد
    from highrise import Highrise
    bot = Highrise()
    await bot.login(room_id, token)
    await bot.join_room(room_id)
    await bot.run(MyBot())

if __name__ == "__main__":
    asyncio.run(run_bot())
