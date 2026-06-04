import os
import threading
import asyncio
from http.server import SimpleHTTPRequestHandler, HTTPServer
from highrise import BaseBot

# ۱. سرور وب فیک برای روشن ماندن در رندر
def run_fake_server():
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(('0.0.0.0', port), SimpleHTTPRequestHandler)
    print(f"Fake server running on port {port}")
    server.serve_forever()

threading.Thread(target=run_fake_server, daemon=True).start()

# ۲. بخش ربات و خوش‌آمداگویی
class MyBot(BaseBot):
    async def on_start(self, session_metadata) -> None:
        print("ربات با موفقیت وارد اتاق شد!")

    async def on_user_join(self, user, position) -> None:
        welcome_message = f"سلام {user.username} عزیز! به اتاق ما خیلی خوش آمدی 🌟"
        await self.highrise.chat(welcome_message)

# ۳. اجرای مستقیم ربات بدون نیاز به دستورات رندر
if __name__ == "__main__":
    room_id = "شناسه_اتاق_شما"  # <--- آی‌دی اتاقت را اینجا بنویس
    token = "توکن_شما"      # <--- توکن رباتت را اینجا بنویس
    
    from highrise.__main__ import ArunBot
    # راه اندازی مستقیم ربات
    asyncio.run(ArunBot().run(MyBot(), room_id, token))
    
