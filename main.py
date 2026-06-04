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
    
    # این دستور جایگزینِ فراخوانیِ دستیِ main می‌شود و از سیستم داخلی خود هایرایز استفاده می‌کند
    sys.argv = ["highrise", "main:MyBot", room_id, token]
    highrise_main.main()

