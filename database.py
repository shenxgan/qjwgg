#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb
import thread

class DataBase():
    def __init__(self):
        self.db_host = 'localhost'
        self.db_user = 'root'
        self.db_passwd = 'password'
        self.db = None
        self.cursor = None
        self.lock = thread.allocate_lock()

    def connect(self):
        try:
            self.db = MySQLdb.connect(host=self.db_host, user=self.db_user, passwd=self.db_passwd, db='qjwgg', charset='utf8')
            self.cursor = self.db.cursor()
        except:
            print 'connect mysql failed!'
            raise

    def disconnect(self):
        try:
            if self.cursor is not None:
                self.cursor.close()
            if self.db is not None:
                self.db.close()
        except:
            pass

    def reconnect(self):
        try:
            self.disconnect()
            self.connect()
        except:
            pass
            
    def _ping(self):
        try:
            self.db.ping()
        except:
            self.reconnect()

    def select(self, sql): ## select
        results = []
        try:
            self.execute(sql)
            results = self.cursor.fetchall()
        except Exception, e:
            pass
        finally:
            return results

    def execute(self, sql): ## insert/update/delete/replace
        try:
            self.lock.acquire()
            self._ping()
            self.cursor.execute(sql)
        except Exception, e:
            pass
        finally:
            self.lock.release()

    def commit(self):
        try:
            self.db.commit()
        except:
            self.db.rollback()

dbhandler = DataBase()
