"""
*This is an example code to show how to communicate with Mysql with store.py
"""
from app.parser import parse_message_info
from dal.entities import Message
from dal.store import MessageStore
import win32com.client

DEFAULT_INDEX_ID = 6
outlook = win32com.client.Dispatch('Outlook.Application').GetNamespace('MAPI')
inbox_folder = outlook.GetDefaultFolder(DEFAULT_INDEX_ID)
import os

if __name__ == "__main__":
    message_store = MessageStore()
    print("[*] Inserting message...")
    message = Message(message_id="123", timestamp="1111000", subject="JackTest", _from="Jack_NB",
                      save_location="Jack_server")
    # insert new user;
    user_data = message_store.insert_new_message(message)
    print("inserted  with ", user_data)

    msg_num = inbox_folder.Items.Count
    messages = []
    for counter in range(msg_num, msg_num - 10, -1):
        message = inbox_folder.Items.Item(counter)
        messages.append(parse_message_info(message))
    for message in messages:
        for key in sorted(message.keys()):
            print(key, "=>", message[key])
        break
