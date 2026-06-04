import os
import asyncio
from highrise import BaseBot
from highrise import __main__ as highrise_main
import sys
from aiohttp import web

# یک سرورِ بسیار ساده برای گول زدنِ رندر که پورتِ مورد نظرش را باز نگه دارد
async def handle(request):
    return web.Response(text="Bot is running!")

class MyBot(BaseBot):
    async def on_start(self, session_metadata) -> None:
        print("ربات با موفقیت در اتاق مستقر شد!")

async def start_server():
    app = web.Application()
    app.router.add_get('/', handle)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', int(os.environ.get("PORT", 8080)))
    await site.start()

async def main():
    # اجرای سرور وب برای جلوگیری از اخراج توسط رندر
    await start_server()
    
    room_id = os.environ.get("ROOM_ID")
    token = os.environ.get("TOKEN")
    
    sys.argv = ["highrise", "main:MyBot", room_id, token]
    highrise_main.main()

if __name__ == "__main__":
    asyncio.run(main())
