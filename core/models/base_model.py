from core.logger import Logger
from core.database import Database

#import requests

class BaseModel:
    TABLE = ''
    FIELDS = ['guid']


    @classmethod
    def findOne(cls, criteria = {}):
        logr = Logger.get_logger(__name__)
        row = Database().get_one('SELECT * FROM %s WHERE ')

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

    @classmethod
    def parse_criteria(cls, criteria):
        result = ''
        for key in criteria:
            if key.upper() == 'NOT':
                result += ' NOT ( %s )' % cls.parse_criteria(criteria[key])
            elif key.upper() in ['AND', 'OR']:
                result += '( '
                #parse each value in criteria[key] and stick key in between them
                innerResults = []
                for innerKey in criteria[key]:
                    innerResults.append(cls.parse_criteria({innerKey: criteria[key[innerKey]]}))
                result += innerResults.join(key.upper())
                result +=' ) '
            else:
                result += '%s = %s' % (key, criteria[key])

        return result



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