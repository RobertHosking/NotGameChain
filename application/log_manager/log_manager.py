import logging, datetime

class DBLoggerManager:

    def __init__(self):
        # Set Database Issues Logging
        self.__db_issues_logger = logging.Logger(name="Database Issues")
        self.__db_issues_logger.setLevel(logging.CRITICAL)
        self.__issues_handler = logging.FileHandler("logs/Database Errors.log")
        self.__issues_handler.setLevel(logging.CRITICAL)
        self.__db_issues_logger.addHandler(self.__issues_handler)

        # Set Database Queries Logging
        self.__db_queries_logger = logging.Logger(name="Database Queries")
        self.__db_queries_logger.setLevel(logging.INFO)
        self.__queries_handler = logging.FileHandler("logs/Database Queries.log")
        self.__queries_handler.setLevel(logging.INFO)
        self.__db_queries_logger.addHandler(self.__queries_handler)

    def getIssuesLogger(self):
        return self.__db_issues_logger

    def getQueriesLogger(self):
        return self.__db_queries_logger


class EmailLogManager:
    def __init__(self):
        # Set Email Logging
        self.__email_logger = logging.Logger(name="Email Logs")
        self.__email_logger.setLevel(logging.INFO)
        self.__email_handler = logging.FileHandler("logs/Email Transactions.log")
        self.__email_handler.setLevel(logging.INFO)
        self.__email_logger.addHandler(self.__email_handler)

    def getEmailLogger(self):
        return self.__email_logger
