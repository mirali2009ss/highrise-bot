import os
import asyncio
from highrise import BaseBot, Highrise
from aiohttp import web

# کلاس ربات تو
class MyBot(BaseBot):
    async def on_start(self, session_metadata) -> None:
        print("ربات با موفقیت در اتاق مستقر شد!")

# سرورِ ساده برای گول زدنِ رندر (برای حالت Web Service)
async def handle(request):
    return web.Response(text="Bot is running!")

async def start_server():
    app = web.Application()
    app.router.add_get('/', handle)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', int(os.environ.get("PORT", 8080)))
    await site.start()

async def main():
    # ۱. اجرای سرور وب
    await start_server()
    
    # ۲. اجرای ربات با روش استاندارد
    room_id = os.environ.get("ROOM_ID")
    token = os.environ.get("TOKEN")
    
    bot = MyBot()
    # استفاده از متدِ صحیح برای اتصال
    await Highrise().run(bot, room_id, token)

if __name__ == "__main__":
    asyncio.run(main())
