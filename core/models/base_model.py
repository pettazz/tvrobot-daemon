from core.logger import Logger
from core.database import Database

#import requests

class BaseModel:
    TABLE = 'Bobby'
    FIELDS = {
        0: 'guid'
    }


    @classmethod
    def findOne(cls, criteria = {}):
        model = cls()
        row = Database().get_one('SELECT * FROM %s WHERE %s ' % (cls.TABLE, cls.parse_criteria(criteria)), {})
        if row:
            model.load(row)
        else:
            model = None
        return model

    @classmethod
    def findAll(cls, criteria = {}):
        rows = Database().get('SELECT * FROM %s WHERE %s ' % (cls.TABLE, cls.parse_criteria(criteria)), {})
        models = []
        for row in rows:
            model = cls()
            model.load(row)
            models.append(model)
        return models

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
            if type(criteria[key]) == dict:
                if key.upper() == 'NOT':
                    result += ' NOT (%s) ' % cls.parse_criteria(criteria[key])
                elif key.upper() in ['AND', 'OR']:
                    result += ' ('
                    #parse each value in criteria[key] and stick key in between them
                    innerResults = []
                    for innerKey in criteria[key]:
                        innerResults.append(cls.parse_criteria({innerKey: criteria[key][innerKey]}))
                    result += key.upper().join(innerResults)
                    result += ') '
                else:
                    Logger.get_logger(__name__).warn('I\'m sorry, I don\'t speak idiot. Couldn\'t parse operator declaration: %s', key)
            else:
                if type(criteria[key]) == str:
                    result += ' %s = "%s" ' % (key, criteria[key])
                else:
                    result += ' %s = %s ' % (key, criteria[key])

        if result == '':
            result = '1'

        return result



    def __init__(self):
        self.logr = Logger.get_logger(__name__)

    def load(self, options):
        if type(options) == dict:
            for opt in options.keys():
                if opt in self.FIELDS.values():
                    setattr(self, opt, options[opt])
                else:
                    self.logr.warning('Unrecognized field `%s` not loaded' % opt)
        elif type(options) in [tuple, list]:
            for idx in range(0, len(options)):
                if idx in self.FIELDS.keys():
                    setattr(self, self.FIELDS[idx], options[idx])
        else:
            self.logr.warning('Attempted to load unknown enum/iterable, ignoring: `%s`' % options)

    def save(self):
        pass