import logging

from tornado.web import RequestHandler


class BaseHandler(RequestHandler):
    
    def __init__(self, application, request, **kwargs):    
        self.logger = logging.getLogger(__name__)

        RequestHandler.__init__(self, application, request, **kwargs)


    def write_error(self, status_code, **kwargs):
        self.logger.error('%s: %s' % (status_code, str(kwargs)))