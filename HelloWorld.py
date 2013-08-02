#__author__ = 'wattanai'

import tornado.ioloop
import tornado.web

from tornado.options import define, options

define("port", default=8888, help="run on the given port", type=int)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world War Z. NXBT ROCKS!!")

application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    tornado.options.parse_command_line()
    application.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()