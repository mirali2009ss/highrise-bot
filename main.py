import os
import threading
from http.server import SimpleHTTPRequestHandler, HTTPServer
from highrise import BaseBot, __main__

# ۱. سرور وب فیک
def run_fake_server():
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(('0.0.0.0', port), SimpleHTTPRequestHandler)
    server.serve_forever()

threading.Thread(target=run_fake_server, daemon=True).start()

# ۲. کلاس ربات
class MyBot(BaseBot):
    async def on_start(self, session_metadata) -> None:
        print("ربات با موفقیت وصل شد!")

# ۳. اجرای مستقیم که متغیرها را از Environment می‌خواند
if __name__ == "__main__":
    # مستقیماً متغیرهای محیطی را می‌خواند
    room_id = os.environ.get("ROOM_ID")
    token = os.environ.get("TOKEN")
    
    # اجرای ربات با استفاده از دستور مستقیم هایرایز
    import sys
    from highrise.__main__ import main
    sys.argv = ["highrise", "main:MyBot", room_id, token]
    main()
    
