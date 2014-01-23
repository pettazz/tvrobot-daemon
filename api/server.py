import logging, time, os
import tornado.ioloop
import tornado.web

import core.config as config
from core.strings import STRINGS

# from core.tvrobot import TVRobot

from api.handlers.sms_handler import SMSHandler
from api.handlers.event_handler import EventHandler

class TVRobotAPI(tornado.web.Application):
    def __init__(self):
        # logging
        logging.basicConfig(
            level = logging.DEBUG,
            format = '%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
            datefmt = '%m-%d %H:%M:%S',
            filename = '%stvrobotd-api.log' % config.TVROBOT['DAEMON']['log_path'],
            filemode = 'a'
        )

        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        logging.getLogger('').addHandler(console)
        self.logger = logging.getLogger(__name__)

        # tvrobot core object
        # self.tvrobot = TvRobot()

        # static handlers
        handlers = [
            (r'/sms', SMSHandler),
            (r'/event', EventHandler),
        ]
        # tornado app settings
        settings = dict(
            debug = False,
            cookie_secret = config.TVROBOT['API']['cookie_secret']
        )
        # init app with settings and static handlers
        tornado.web.Application.__init__(self, handlers, **settings)

        self.logger.info('Application initialized successfully')
        self.logger.info(os.getpid())

def APIRunner():
    # create the API app and start listening
    app = TVRobotAPI()
    app.listen(config.TVROBOT['API']['host_port'])

    # main ioloop
    main_loop = tornado.ioloop.IOLoop.instance()

    # create scheduled tasks
    # # cleanup
    # cleanup_schedule = tornado.ioloop.PeriodicCallback(
    #     app.tvrobot.cleanup_downloads, 
    #     3000000,
    #     io_loop = main_loop
    # )
    # cleanup_schedule.start()
    
    # # look for scheduled downloads
    # downloads_schedule = tornado.ioloop.PeriodicCallback(
    #     app.tvrobot.add_scheduled_downloads, 
    #     3000000,
    #     io_loop = main_loop
    # )
    # downloads_schedule.start()

    # # check for schedule updates
    # updates_schedule = tornado.ioloop.PeriodicCallback(
    #     app.tvrobot.update_schedules, 
    #     3000000,
    #     io_loop = main_loop
    # )
    # updates_schedule.start()

    # welp, let's go
    main_loop.start()