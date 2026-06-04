import os
from highrise import BaseBot
from highrise.__main__ import main

class MyBot(BaseBot):
    async def on_start(self, classroom_id: str, session_id: str, session_metadata: any) -> None:
        
        print("ربات آنلاین شد!")

if __name__ == "__main__":
    main()
  
