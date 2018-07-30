from unittest import TestCase
from app.parser import *
import win32com.client

outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
msg = outlook.OpenSharedItem(
    "C://Users//jack_tsai//PycharmProjects//SQLAlchemy_pysql//Unittest//test_message/test1.msg")


class TestParser(TestCase):
    def test_get_file_type(self):
        test_cases = ["test1.xls", "test2.pdf", "test3.png", "test4.msg"]
        expected = ["application/vnd.ms-excel", "application/pdf", "image/png", ".msg"]
        for test_file in test_cases:
            file_name = get_file_type(test_file)
            self.assertIn(file_name, expected, "%s is not in the expected extension" % file_name)

    def test_parsed_attachment(self):
        attachment = parsed_attachment(msg.Attachments[0])
        self.assertEqual(attachment['file_name'], "image003.jpg", "file_name is wrong!!")
        self.assertEqual(attachment['attachment_id'], 1, "attachment_id is wrong !!")

    def test_parse_message_attachment(self):
        attachments = parse_message_attachment(msg)
        self.assertTrue(len(attachments) > 0, "attachment count should be 1 ")
        self.assertEqual(attachments[0]['message_id'], "9881a59a4ff54b489e1863d22f5ef3b4@asus.com",
                         "message_id not match")

    def test_parse_message_info(self):
        message_dic = parse_message_info(msg)
        self.assertEqual(7, len(message_dic), "dic count should be 7")
        self.assertEqual(message_dic['message_id'], "9881a59a4ff54b489e1863d22f5ef3b4@asus.com", "message_id not match")
        self.assertEqual(message_dic['timestamp'], 1532347321)
