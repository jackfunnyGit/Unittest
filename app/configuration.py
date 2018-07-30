MYSQL_DB_PATH = 'mysql+pymysql://root:1234@10.78.20.122:3306/PI_database'
USERNAME = "root"
PASSWORD = "1234"
IP_ADDRESS_OF_MYSQL_SERVER = "10.78.20.122:3306"
DATABASE_NAME = "PI_database"

connection_strings = {
    "main": "mysql+pymysql://"
            + USERNAME + ":"
            + PASSWORD + "@"
            + IP_ADDRESS_OF_MYSQL_SERVER + "/"
            + DATABASE_NAME
            + "?charset=utf8mb4"
}
"""
* Below is used for email message  
"""

# properties of the message headers
PR_TRANSPORT_MESSAGE_HEADERS = "http://schemas.microsoft.com/mapi/proptag/0x007D001F"
# properties of the smtp address
PR_SMTP_ADDRESS = "http://schemas.microsoft.com/mapi/proptag/0x39FE001E"


