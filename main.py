import os
import threading
import asyncio
from http.server import SimpleHTTPRequestHandler, HTTPServer
from highrise import BaseBot, Bot

# ۱. سرور فیک برای زنده ماندن رندر
def run_fake_server():
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(('0.0.0.0', port), SimpleHTTPRequestHandler)
    server.serve_forever()

# ۲. کلاس ربات با مدیریت ساده
class MyBot(BaseBot):
    async def on_start(self, session_metadata) -> None:
        print("ربات با موفقیت آنلاین شد!")

# ۳. اجرای ایزوله و دقیق ربات
async def main():
    room_id = os.environ.get("ROOM_ID")
    token = os.environ.get("TOKEN")
    
    # اطمینان از وجود متغیرها
    if not room_id or not token:
        print("Error: ROOM_ID or TOKEN missing!")
        return

    bot = MyBot()
    # استفاده از متد run که در تمام نسخه‌ها استاندارد است
    await Bot(bot, room_id, token).run()

if __name__ == "__main__":
    # استارت سرور وب
    threading.Thread(target=run_fake_server, daemon=True).start()
    # اجرای حلقه رویداد ربات
    asyncio.run(main())
