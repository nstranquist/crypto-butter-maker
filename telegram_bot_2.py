import asyncio
from telethon.sync import TelegramClient
from telethon import events, sync
from telethon.tl.functions.messages import (GetHistoryRequest)
from telethon.tl.types import (
PeerChannel
)
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty

api_id = 000000
api_hash = 'yourhash'
phone = "+yourphone"

client = TelegramClient(phone, api_id, api_hash)



chat_group_id = 1284847365
chat_group_name = "GG-Shot Notifications"

# listen to new messages
@client.on(events.NewMessage(chats=chat_group_id))
async def newMessageListener(event):
  try:
    if event.message.message:
      newMessage = event.message.message
      print("Message: " + newMessage, end="\n\n")
      print("All Message Data: " + str(event.message))
      print("Button Count: " + event.message.button_count)
      buttons = event.message.buttons

      for button in buttons:
        print("Button: " + str(button))

      # Find The Relevant data points
      trade_side_index = newMessage.find("LONG")
      trade_side="none"
      if trade_side_index < 0:
        trade_side_index = newMessage.find("SHORT")
        if trade_side_index < 0:
          raise Exception("Short / Long not found in this message!")
        else:
          trade_side = "SHORT"
      else:
        trade_side = "LONG"
          
      entry_index = newMessage.find("Enrty")
      if entry_index > -1:
        print("found entry! It is at index: " + entry_index + ", and the char is: " + newMessage[entry_index])
        entry_value = ""
        first_entry_index = entry_index + 6 # 5 chars for "Enrty" + 1 char for ":" + 1

        is_numeric = True
        index = first_entry_index

        while is_numeric and index < len(newMessage):
          current_char = newMessage[index]
          print("next char is: " + current_char)
          if not current_char.is_numeric():
            is_numeric = False
          else:
            entry_value = entry_value + current_char
            index = index + 1

      
  except Exception as exc:
    print("Exception: " + str(exc))

with client:
  client.connect()
  if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input("Enter the code: "))
  # after logging in, the .session file will be created. It's a database file to make the session persistent

  client.run_until_disconnected()

# List All Telegram Groups
# chats = []
# last_date = None
# chunk_size = 200
# groups = []

# chat_history = []



# dialogs_result = client(GetDialogsRequest(
#   offset_date = last_date,
#   offset_id = 0,
#   offset_peer = InputPeerEmpty(),
#   limit = chunk_size,
#   hash = 0
# ))
# chats.extend(dialogs_result.chats)

# chat_name = "GG-Shot Notifications"

# for chat in chats:
#   try:
#     print("chat name: " + chat.title)
#     if chat.title == chat_name:
#       print("found group")
#       # Get Chat Data

#   except Exception as exc:
#     print("exception: " + str(exc))

# # for chat in chats:
# #   try:
# #     print("Chat:", end=" ")
# #     print(chat, end="\n\n")
# #     if chat.megagroup == True:
# #       groups.append(chat)
# #   except:
# #     continue

# # print("Choose a group to scrape members from:")
# # i = 0
# # for group in groups:
# #   print(str(i) + "- " + group.title)
# #   i+=1

# # group_index = input("Enter a Number: ")
# # target_group = groups[int(group_index)]

# # Get All Participants
# # print('Fetching Members...')
# # all_participants = []
# # all_participants = client.get_participants(target_group, aggressive=True)