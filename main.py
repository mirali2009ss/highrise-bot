import os
import asyncio
from highrise import BaseBot
from highrise import __main__ as highrise_main
import sys

class MyBot(BaseBot):
    async def on_start(self, session_metadata) -> None:
        print("ربات با موفقیت در اتاق مستقر شد!")

if __name__ == "__main__":
    room_id = os.environ.get("ROOM_ID")
    token = os.environ.get("TOKEN")
    
    # تنظیم آرگومان‌ها
    sys.argv = ["highrise", "main:MyBot", room_id, token]
    
    # استفاده از دستور اصلی برای اجرای دائمی
    # این دستور تا زمانی که ربات در اتاق است، برنامه را زنده نگه می‌دارد
    highrise_main.main()
