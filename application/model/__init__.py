import pymysql.cursors, logging, datetime
from application.log_manager import DBLoggerManager

class SQLDatabase:

    def __init__(self, conn_cred):
        self.connection_cred = conn_cred
        self.loggerManager = DBLoggerManager()
        self.issues_logger = self.loggerManager.getIssuesLogger()
        self.queries_logger = self.loggerManager.getQueriesLogger()
        self.connection = None
        try:
            self.connection = pymysql.connect(
                host=self.connection_cred['cred']['db_cred']['host'],
                user=self.connection_cred['cred']['db_cred']['user'],
                password=self.connection_cred['cred']['db_cred']['password'],
                db=self.connection_cred['cred']['db_cred']['db'],
                charset=self.connection_cred['cred']['db_cred']['charset'],
                cursorclass=pymysql.cursors.DictCursor
            )
            self.queries_logger.log(
                logging.INFO, "Connected!"
            )

        except Exception as e:
            self.issues_logger.log(
                logging.CRITICAL, "Connection failed. Info: \n{0}".format(e.message)
            )

    def insert(self, sql):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sql)
                self.connection.commit()
            self.queries_logger.log(
                logging.INFO, "Queried OK")
            return True
        except Exception as e:
            self.issues_logger.log(
                logging.CRITICAL, "Insertion failed. Info: \n{0}".format(e.message)
            )
            return False

    def query(self, sql):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sql)
                result = cursor.fetchall()
            self.queries_logger.log(
                logging.INFO, "Queried OK")
            return result
        except Exception as e:
            self.issues_logger.log(
                logging.CRITICAL, "Queried failed. Info: \n{0}".format(e.message)
            )

    def __del__(self):
        self.connection.close()