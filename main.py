import os
import threading
from http.server import SimpleHTTPRequestHandler, HTTPServer
from highrise import BaseBot, __main__
from highrise.models import SessionMetadata, User, Position

# ۱. سرور وب فیک برای روشن ماندن در رندر
def run_fake_server():
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(('0.0.0.0', port), SimpleHTTPRequestHandler)
    print(f"Fake server running on port {port}")
    server.serve_forever()

threading.Thread(target=run_fake_server, daemon=True).start()

# ۲. بخش اصلی ربات با متدهای استاندارد و ایمن
class MyBot(BaseBot):
    async def on_start(self, session_metadata: SessionMetadata) -> None:
        print("ربات با موفقیت آنلاین شد و به اتاق وصل گردید!")

    # متد کاملاً استاندارد برای تشخیص ورود بازیکنان
    async def on_user_join(self, user: User, position: Position | None) -> None:
        try:
            welcome_message = f"سلام {user.username} عزیز! به اتاق ما خیلی خوش آمدی 🌟"
            await self.highrise.chat(welcome_message)
        except Exception as e:
            print(f"Error in welcome: {e}")

if __name__ == "__main__":
    # اجرای خودکار با متد اصلی پکیج
    __main__.main()
    
