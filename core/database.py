from core.logger import Logger
import core.config as config

import time

import MySQLdb

class Database:
    def __init__(self):
        self.logr = Logger.get_logger(__name__)
        self._conn = None
        self._conn = self.__get_conn()

    def __get_conn(self):
        if self._conn is None:
            self._conn = self.__open_db()
        return self._conn

    def __open_db(self):
        retry_count = config.database['mysql']['retries']
        backoff = config.database['mysql']['backoff']
        count = 0
        while count < retry_count:
            try:
                self.logr.info('attempting to connect to MySQL db (#%s)' % (count + 1))
                conn = MySQLdb.connect(
                    host   = config.database['mysql']['server'],
                    user   = config.database['mysql']['user'],
                    passwd = config.database['mysql']['password'],
                    db     = config.database['mysql']['schema'])
                conn.autocommit(True)
                self.logr.info('successfully connected to MySQL database `%s`' % config.database['mysql']['schema'])

                return conn
            except Exception, e:
                self.logr.warn('failed to connect to MySQL db: %s' % repr(e))
                count = count + 1
                # don't bother waiting if we already plan to bail 
                if count < retry_count:
                    self.logr.info('waiting %s seconds to retry' % backoff)
                    time.sleep(backoff)
            
        if count >= retry_count:
            self.logr.error('MySQL connection attempt retry count exceeded, giving up.')
            raise ConnectionFailureError(' after %s retries.')

    def __close_db(self):
        self.logr.info('closing MySQL db connection')
        conn = self.__get_conn()
        conn.cursor().close()
        conn.close()
        self._conn = None

    def __sanitize(self, value):
        if type(value) == dict:
            retval = {}
            for key in value:
                if type(value[key]) == str:
                    escaped_val = self.__get_conn().escape_string(value[key])
                else:
                    escaped_val = value[key]
                retval[key] = escaped_val

        elif type(value) == str:
            retval = self.__get_conn().escape_string(value)

        else:
            retval = value

        return retval


    def query(self, query, values = {}):
        values = self.__sanitize(values)
        self.logr.info('Executing MySQL query: `%s`' % (query % values))
        cursor = self.__get_conn().cursor()
        cursor.execute(query, values)
        return cursor

    def get_one(self, query, values):
        cursor = self.query(query, values)
        return cursor.fetchone()

    def get(self, query, values):
        cursor = self.query(query, values)
        return cursor.fetchall()


class ConnectionFailureError(Exception):
    def __init__(self, retries = 0):
        message = 'Unable to connect to MySQL Database'
        if retries > 0:
            message = message + ' after %s retries.' % retries
        else:
            message = message + '.'
        Exception.__init__(self, message)