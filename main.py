import os
import asyncio
from highrise import BaseBot
from highrise import __main__ as highrise_main
import sys
from aiohttp import web

class MyBot(BaseBot):
    async def on_start(self, session_metadata) -> None:
        print("ربات در اتاق مستقر شد!")

async def web_server(request):
    return web.Response(text="Bot is running")

async def main():
    # ۱. راه اندازی سرور برای جلوگیری از بسته شدن ربات توسط رندر
    app = web.Application()
    app.router.add_get('/', web_server)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', int(os.environ.get("PORT", 8080)))
    await site.start()

    # ۲. اجرای خود ربات
    room_id = os.environ.get("ROOM_ID")
    token = os.environ.get("TOKEN")
    sys.argv = ["highrise", "main:MyBot", room_id, token]
    highrise_main.main()

if __name__ == "__main__":
    asyncio.run(main())
