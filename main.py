import os
import threading
from http.server import SimpleHTTPRequestHandler, HTTPServer
from highrise import BaseBot
from highrise.__main__ import main
from highrise.models import SessionMetadata, User

# ۱. سرور وب فیک برای روشن ماندن در رندر
def run_fake_server():
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(('0.0.0.0', port), SimpleHTTPRequestHandler)
    print(f"Fake server running on port {port}")
    server.serve_forever()

threading.Thread(target=run_fake_server, daemon=True).start()

# ۲. بخش ربات و خوش‌آمدگویی
class MyBot(BaseBot):
    async def on_start(self, session_metadata: SessionMetadata) -> None:
        print("ربات آنلاین شد و آماده خوش‌آمدگویی است!")

    # این تابع به محض ورود هر نفر خودکار اجرا می‌شود
    async def on_user_join(self, user: User, position) -> None:
        # متن پیام خوش‌آمدگویی (می‌توانی این متن را به دلخواه خودت تغییر بدهی)
        welcome_message = f"سلام {user.username} عزیز! به اتاق ما خیلی خوش آمدی 🌟"
        
        # فرستادن پیام در چت اتاق
        await self.highrise.chat(welcome_message)

if __name__ == "__main__":
    main()
    
