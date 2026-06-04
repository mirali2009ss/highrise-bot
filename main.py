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
    
    # این دستور آرگومان‌های لازم را به صورت شبیه‌سازی شده به تابع اصلی می‌دهد
    sys.argv = ["highrise", "main:MyBot", room_id, token]
    
    # برای دور زدن خطای آرگومان، از یک فراخوانیِ مستقیم استفاده می‌کنیم
    try:
        highrise_main.main()
    except TypeError:
        # اگر همچنان خطای آرگومان داد، این متد جایگزین را اجرا می‌کنیم
        from highrise.models import SessionMetadata
        highrise_main.main(definitions=None)
        

