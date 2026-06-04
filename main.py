import os
import asyncio
from highrise import BaseBot
from highrise import __main__ as highrise_main
import sys

class MyBot(BaseBot):
    async def on_start(self, session_metadata) -> None:
        print("ربات با موفقیت در اتاق مستقر شد!")

async def main():
    room_id = os.environ.get("ROOM_ID")
    token = os.environ.get("TOKEN")
    
    if not room_id or not token:
        print("خطا: ROOM_ID یا TOKEN تنظیم نشده‌اند!")
        return

    # اصلاح نهایی برای جلوگیری از ارورِ آرگومانِ گمشده
    # ما از یک تابعِ پوششی استفاده می‌کنیم تا آرگومان‌های اضافه را نادیده بگیرد
    def run_bot():
        sys.argv = ["highrise", "main:MyBot", room_id, token]
        highrise_main.main()
    
    run_bot()

if __name__ == "__main__":
    asyncio.run(main())
