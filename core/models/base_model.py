from core.logger import Logger
from core.database import Database

#import requests

class BaseModel:
    TABLE = ''
    FIELDS = ['guid']


    @classmethod
    def findOne(cls, criteria = {}):
        logr = Logger.get_logger(__name__)
        # row = Database().get_one('SELECT * FROM %s WHERE ')

    @classmethod
    def findAll(cls, criteria = {}):
        logr = Logger.get_logger(__name__)
        pass

    @classmethod
    def search(cls, criteria = {}):
        logr = Logger.get_logger(__name__)
        pass

    @classmethod
    def create(cls, self):
        logr = Logger.get_logger(__name__)
        pass


    def __init__(self, data = None):
        self.logr = Logger.get_logger(__name__)

        if data is None:
            self.create()

    def load(self, options):
        for opt in options.keys():
            if opt in self.FIELDS:
                setattr(self, opt, options[opt])
            else:
                self.logr.warning('Unrecognized field `%s` not loaded' % opt)

    def save(self):
        pass