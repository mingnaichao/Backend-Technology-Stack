# -*- coding: utf-8 -*-
# @author : MingNC
# @description: 
# @date : 2019/12/21
# @time : 21:43
import datetime

import tornado.web
import tornado.ioloop
import tornado.httpserver
from tornado.options import define, options

define("port", default='8001', help='Config File', type=int)


class PingHandler(tornado.web.RequestHandler):
    """
    健康检查
    """

    def data_received(self, chunk):
        pass

    def get(self, *args):
        print("args:{}".format(args))
        self.write("Hello get,i'm mingnc:{}".format(datetime.datetime.now()))

    def post(self, *args):
        print("args:{}".format(args))
        self.write("Hello post,i'm mingnc:{}".format(datetime.datetime.now()))

    def head(self, *args, **kwargs):
        print("args:{}".format(args))
        print("kwargs:{}".format(kwargs))
        self.write('Hi head:{}'.format(datetime.datetime.now()))

    def options(self, *args, **kwargs):
        print("args:{}".format(args))
        print("kwargs:{}".format(kwargs))

        self.set_header('Access-Control-Allow-Methods', 'POST,GET')
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Headers', 'Authorization,Content-type')
        self.set_status(204)
        self.finish()


if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application([
        (r"/ping", PingHandler)
    ], debug=True, websocket_ping_interval=0)

    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    print("Docker test Service Started on port {} !".format(options.port))
    tornado.ioloop.IOLoop.instance().start()
