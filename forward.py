import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession
import os

API_ID = 33790522
API_HASH = '00e4131295f55452e143c06099c1ddae'
SESSION_STRING = os.environ.get('SESSION_STRING')

async def main():
    if not SESSION_STRING:
        print("❌ SESSION_STRING not found!")
        return
    
    client = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)
    await client.start()
    
    source = '@hamody_up4'
    targets = ['@CC428Kurd']
    
    last_message_id = None
    
    while True:
        try:
            async for message in client.iter_messages(source, limit=1):
                if last_message_id is None or message.id != last_message_id:
                    for target in targets:
                        await client.forward_messages(target, message)
                        print(f"✅ Forwarded: {message.id}")
                    last_message_id = message.id
                else:
                    print("⏳ No new cards")
        except Exception as e:
            print(f"❌ Error: {e}")
        
        await asyncio.sleep(30)

asyncio.run(main())
