# -*- coding: utf-8 -*-
# @author : MingNC
# @date : 2019/11/25
# @time : 23:01
import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options
from tornado.options import define, options

define("port", default=8866, help="run on given port", type=int)


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        greeting = self.get_argument('greeting', 'hello')
        self.write(greeting + ', friendly user!')

    def write_error(self, chunk, **kwargs):
        self.write('this is a error:{}'.format(chunk))


if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[
        ("./", IndexHandler)
    ])

    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
