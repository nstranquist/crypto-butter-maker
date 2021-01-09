from telethon import TelegramClient, events

# class TelegramBot:
#   def __init__(self, api_id, api_hash):
#     self.bot_token = str(api_id) + ":" + api_hash
#     self.bot = TelegramClient('bot', api_id, api_hash).start(bot_token = self.bot_token)

api_id = 000000
api_hash = 'your-hash'
bot_token = str(api_id) + ":" + api_hash

client = TelegramClient('anon', api_id, api_hash)

@client.on(events.NewMessage(chats='channel_name'))
async def my_event_handler(event):
  print("Event:", end=" ")
  print(event.raw_text)

client.start()
client.run_until_disconnected()

# first param is .session file name (absolute paths allowed)
# with TelegramClient('name', api_id, api_hash) as client:
#   client.send_message