import os
import threading
from http.server import SimpleHTTPRequestHandler, HTTPServer
from highrise import BaseBot

# سرور فیک برای رندر
def run_fake_server():
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(('0.0.0.0', port), SimpleHTTPRequestHandler)
    server.serve_forever()

threading.Thread(target=run_fake_server, daemon=True).start()

# کلاس ربات (فقط BaseBot)
class MyBot(BaseBot):
    async def on_start(self, session_metadata) -> None:
        print("ربات با موفقیت آنلاین شد!")

if __name__ == "__main__":
    from highrise.__main__ import main
    import sys
    
    # گرفتن مستقیم متغیرها
    room_id = os.environ.get("ROOM_ID")
    token = os.environ.get("TOKEN")
    
    # اجرای مستقیم
    sys.argv = ["highrise", "main:MyBot", room_id, token]
    main()
