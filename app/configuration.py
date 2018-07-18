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
}
