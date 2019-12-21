# -*- coding: utf-8 -*-
# @author : mingnaichao
# @date : 2019/10/2
# @time : 14:18

# from importlib import reload
# import __future__
# import sys
import ssl

import tornado.web
import tornado.ioloop
import tornado.httpserver
from tornado.options import define, options

from handlers import VoiceToVoiceHandler, VoiceToTextHandler, TextToTextHandler, TextToVoiceHandler

ssl._create_default_https_context = ssl._create_unverified_context
# reload(sys)
# sys.setdefaultencoding('utf-8')  # 处理编码问题

define("port", default='8866', help='Config File', type=int)


class PingHandler(tornado.web.RequestHandler):
    """
    健康检查
    """

    def data_received(self, chunk):
        pass

    def get(self, *args):
        print(args)

        self.write("Hello,i'm mingnc")

    def post(self, *args):
        print(args)

        self.write("Hello,i'm mingnc")

    def head(self, *args, **kwargs):
        print(args)
        print(kwargs)

        self.write('Hi')

    def options(self, *args, **kwargs):
        print(args)
        print(kwargs)

        self.set_header('Access-Control-Allow-Methods', 'POST,GET')
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Headers', 'Authorization,Content-type')
        self.set_status(204)
        self.finish()


if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application([
        (r"/ai_recruit/voice_to_voice", VoiceToVoiceHandler),
        (r"/ai_recruit/voice_to_text", VoiceToTextHandler),
        (r"/ai_recruit/text_to_text", TextToTextHandler),
        (r"/ai_recruit/text_to_voice", TextToVoiceHandler),
        (r"/ping", PingHandler)
    ], debug=True, websocket_ping_interval=0)

    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    print("HCM Ai Recruit Service Started on port {} !".format(options.port))
    tornado.ioloop.IOLoop.instance().start()
