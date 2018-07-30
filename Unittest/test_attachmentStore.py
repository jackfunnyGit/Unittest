from unittest import TestCase

import win32com.client

outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
msg = outlook.OpenSharedItem(
    "C://Users//jack_tsai//PycharmProjects//SQLAlchemy_pysql//Unittest//test_message/test1.msg")


class TestAttachmentStore(TestCase):
    def test__transfer_to_entities(self):
        pass

    def test_insert_new_attachment(self):
        pass
