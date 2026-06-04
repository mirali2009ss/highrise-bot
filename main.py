import os
import threading
from http.server import SimpleHTTPRequestHandler, HTTPServer
from highrise import BaseBot, Bot

class MyBot(BaseBot):
    async def on_start(self, session_metadata) -> None:
        print("ربات با موفقیت وصل شد!")

def run_fake_server():
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(('0.0.0.0', port), SimpleHTTPRequestHandler)
    server.serve_forever()

if __name__ == "__main__":
    threading.Thread(target=run_fake_server, daemon=True).start()
    
    room_id = os.environ.get("ROOM_ID")
    token = os.environ.get("TOKEN")
    
    bot = MyBot()
    Bot().run(bot, room_id, token)
