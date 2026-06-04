import os
import threading
import asyncio
from http.server import SimpleHTTPRequestHandler, HTTPServer
from highrise import BaseBot, Bot

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

# ۳. اجرای استاندارد با تصحیح کامل متغیرها
async def main():
    # بر اساس تایید شما، جای این دو دقیقاً برعکس شد:
    token = "a41a7ec0025b83462a07db640c5abb3d6ac2dfbbef501530db87517f17895a09"
    room_id = "6569747fff370b7aa794b600"
    
    bot_instance = MyBot()
    await Bot().run(bot_instance, room_id, token)

if __name__ == "__main__":
    asyncio.run(main())
    
