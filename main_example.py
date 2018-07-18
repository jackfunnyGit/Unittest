"""
*This is an example code to show how to communicate with Mysql with store.py
"""
from dal.entities import MessageTable
from dal.store import MessageStore

if __name__ == "__main__":
    message_store = MessageStore()
    print("[*] Inserting message...")
    message = MessageTable(messageId=112, subject="JackTest", _from="Jack_NB", saveLocation="Jack_server")
    # insert new user;
    user_data = message_store.insert_new_message(message)
    print("inserted  with ", user_data)
