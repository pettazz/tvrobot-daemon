import logging, os

import core.config as config

def singleton(cls):
    instances = {}
    def get_instance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return get_instance()

@singleton
class Logger:
    def __init__(self, logger_name = 'root'):
        if not os.path.exists(config.tvrobot['daemon']['log_path']):
            os.makedirs(config.tvrobot['daemon']['log_path'])
        self.logger_name = logger_name
        self.logger = self.__init_logger(self.logger_name)

    def __init_logger(self, logger_name):
        logging.basicConfig(
            level = logging.DEBUG,
            format = '%(asctime)s [%(levelname)s] %(name)s:%(funcName)s() %(message)s',
            datefmt = '%m-%d %H:%M:%S',
            filename = '%stvrobotd-%s.log' % (config.tvrobot['daemon']['log_path'], logger_name),
            filemode = 'a'
        )

        console = logging.StreamHandler()
        logging.getLogger('').addHandler(console)
        self.logger = logging.getLogger(logger_name)

    def __kill_logger(self):
        self.logger = None

    def get_logger(self, name = None):

        if name is None:
            name = self.logger_name

        if self.logger is None:
            self.__init_logger(name)

        return self.logger
