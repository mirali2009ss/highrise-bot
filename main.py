import os
import threading
from http.server import SimpleHTTPRequestHandler, HTTPServer
from highrise import BaseBot

# ۱. سرور وب فیک برای روشن ماندن در رندر
def run_fake_server():
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(('0.0.0.0', port), SimpleHTTPRequestHandler)
    print(f"Fake server running on port {port}")
    server.serve_forever()

threading.Thread(target=run_fake_server, daemon=True).start()

# ۲. کلاس اصلی ربات و خوش‌آمداگویی
class MyBot(BaseBot):
    async def on_start(self, session_metadata) -> None:
        print("ربات با موفقیت آنلاین شد و به اتاق وصل گردید!")

    async def on_user_join(self, user, position) -> None:
        welcome_message = f"سلام {user.username} عزیز! به اتاق ما خیلی خوش آمدی 🌟"
        await self.highrise.chat(welcome_message)
        
