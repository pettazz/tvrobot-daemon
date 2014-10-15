from core.logger import Logger

#import requests

class BaseModel:

    FIELDS = []

    def __init__(self):
        self.logr = Logger.get_logger(__name__)

    def load(self, options):
        for opt in options.keys():
            if opt in self.FIELDS:
                setattr(self, opt, options[opt])
            else:
                self.logr.warning('Unrecognized field `%s` not loaded' % opt)