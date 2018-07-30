from unittest import TestCase

import win32com.client

from app.parser import parse_message_info
from dal.store import MessageStore

outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
msg = outlook.OpenSharedItem(
    "C://Users//jack_tsai//PycharmProjects//SQLAlchemy_pysql//Unittest//test_message/test1.msg")


class TestMessageStore(TestCase):
    def test__transfer_to_entity(self):
        message_dic = parse_message_info(msg)
        message = MessageStore()._transfer_to_entity(message_dic)
        self.assertEqual(message.message_id, "9881a59a4ff54b489e1863d22f5ef3b4@asus.com", "message_id is wrong")

    def test_insert_new_message(self):
        message_dic = parse_message_info(msg)
        MessageStore().insert_new_message(message_dic)
