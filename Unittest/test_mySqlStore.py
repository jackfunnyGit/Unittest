from unittest import TestCase
from dal.store import MySqlStore
from dal.entities import MessageTable

MYSQL_URL = 'mysql+pymysql://root:1234@10.78.20.122:3306/Unittest_db'
MYSQL_CREATE_TEST_TABLE = "CREATE TABLE IF NOT EXISTS `UnitestTable`(\
                               `id` INT NOT NULL AUTO_INCREMENT,\
                               `messageId` INT UNSIGNED NOT NULL,\
                               `subject` TEXT NOT NULL,\
                               `from` TEXT NOT NULL,\
                               `saveLocation` TEXT NOT NULL,\
                               PRIMARY KEY(id)\
                               );"
MYSQL_DROP_TEST_TABLE = "DROP DATABASE UnitestTable;"


class TestMySqlStore(TestCase):
    def get_attr(self):
        pass

    def setUp(self):
        print("setUp...")
        self.message = MessageTable(messageId=112, subject="JackTest", _from="Jack_NB", saveLocation="Jack_server")

    def tearDown(self):
        print("tearDown...")

    def test_create_object(self):
        MySqlStore.create_object(self.message)
        self.assertTrue(self.message.id > 0, "instance id should not be less than 0 ")

    def test_read_object(self):
        data = MySqlStore.read_object(MessageTable)
        self.assertTrue(len(data) > -1, "data count should be 0 or larger than 0")

    def test_update_object(self):
        MySqlStore.create_object(self.message)
        update_message = MySqlStore.update_object(self.message, {"subject": "TTTT"})
        self.assertNotEqual(self.message.subject, update_message.subject, "subject attribute should be changed ")

    def test_delete_object(self):
        MySqlStore.create_object(self.message)
        result = MySqlStore.delete_object(self.message.id, MessageTable)
        self.assertFalse(result, "deleted result should be true ")
