# -*- coding: utf-8 -*-
# @author : MingNC
# @date : 2019/11/24
# @time : 18:39
import tornado.web
from user_handlers import user_handler
import tornado.ioloop
import tornado.httpserver

HANDLERS = [
    ('/api/users', user_handler.UserListHandler),
    ('/api/users/(\d+)', user_handler.UserHandler)
]


def run():
    app = tornado.web.Application(
        HANDLERS,
        debug=True
    )
    http_server = tornado.httpserver.HTTPServer(app)
    port = 8888
    http_server.listen(port)
    print('http server port {}'.format(port))
    tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    run()
