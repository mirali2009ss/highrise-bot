import os
import asyncio
from highrise import BaseBot, Highrise
from aiohttp import web

class MyBot(BaseBot):
    async def on_start(self, session_metadata) -> None:
        print("ربات با موفقیت در اتاق مستقر شد!")

async def handle(request):
    return web.Response(text="Bot is running")

async def start_server():
    app = web.Application()
    app.router.add_get('/', handle)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', int(os.environ.get("PORT", 8080)))
    await site.start()

async def main():
    await start_server()
    room_id = os.environ.get("ROOM_ID")
    token = os.environ.get("TOKEN")
    
    # روشِ استاندارد برای اجرای ربات که در تمام نسخه‌ها جواب می‌دهد
    bot = MyBot()
    # در نسخه‌های جدید، باید از Highrise() برای مدیریت استفاده کنیم 
    # و با متدِ زیر ربات را متصل کنیم:
    definitions = [] 
    await Highrise(bot).connect(room_id, token)

if __name__ == "__main__":
    asyncio.run(main())
