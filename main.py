import os
import threading
from http.server import SimpleHTTPRequestHandler, HTTPServer
from highrise import BaseBot
from highrise.__main__ import main

# ۱. ساخت یک سرور وب فیک برای فریب دادن رندر
def run_fake_server():
    # رندر پورت را به صورت خودکار در متغیر PORT قرار می‌دهد، اگر نبود روی 10000 تنظیم می‌شود
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(('0.0.0.0', port), SimpleHTTPRequestHandler)
    print(f"Fake server running on port {port}")
    server.serve_forever()

# اجرای سرور فیک در یک ترید جداگانه تا مزاحم ربات نشود
threading.Thread(target=run_fake_server, daemon=True).start()

# ۲. کلاس ربات شما
class MyBot(BaseBot):
    async def on_start(self, session_metadata: any) -> None:
        print("ربات آنلاین شد!")

if __name__ == "__main__":
    main()
    
