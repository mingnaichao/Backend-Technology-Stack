# -*- coding: utf-8 -*-
# @author : MingNC
# @date : 2019/11/18
# @time : 22:57
import os

import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        # self.write("Hello, world")
        self.render('base.html')


class ErrorHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('500.html', msg="后台有错，请重试")


def make_app():
    return tornado.web.Application(
        [
            (r"/", MainHandler),
            (r"/500", ErrorHandler)
        ],
        template_path=os.path.join(
            os.path.dirname(__file__), 'templates'
        ),
        debug=True
    )


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
