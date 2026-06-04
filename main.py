 import os
import asyncio
from highrise import BaseBot
from highrise import __main__ as highrise_main

class MyBot(BaseBot):
    async def on_start(self, session_metadata) -> None:
        print("ربات با موفقیت در اتاق مستقر شد!")

async def main():
    # دریافت اطلاعات از محیط
    room_id = os.environ.get("ROOM_ID")
    token = os.environ.get("TOKEN")
    
    if not room_id or not token:
        print("خطا: ROOM_ID یا TOKEN تنظیم نشده‌اند!")
        return

    # روش صحیح فراخوانی بدون نیاز به کلاس Bot که ارور می‌داد
    # به جای Bot(bot, ...).run() از متد اصلی استفاده می‌کنیم
    import sys
    sys.argv = ["highrise", "main:MyBot", room_id, token]
    highrise_main.main()

if __name__ == "__main__":
    # اجرای حلقه
    asyncio.run(main())
    
