# -*- coding: utf-8 -*-
# @author : MingNC
# @date : 2019/12/10
# @time : 21:48
import logging

import tornado.web
from aai_request import AaiRequest
from tbp_request import TbpRequest


class VoiceToVoiceHandler(tornado.web.RequestHandler):
    """
    输入语音，输出语音
    """

    def data_received(self, chunk):
        pass

    def get(self):
        pass

    def post(self, *args, **kwargs):
        session_id = self.get_argument('session_id')
        voice_data = self.get_argument('voice_data')

        bot_id = "f8af9c03-bf86-4d45-a571-93dd3af8fda0"
        secret_id = 'AKIDf5IHsMxeS4ScZGkFwQgkcHl7E7lZLTZO'
        secret_key = 'knlTvAlPofIiuqa5RYimeGdsrdqrfmgO'

        aai_request = AaiRequest(
            secret_id=secret_id,
            secret_key=secret_key,
            session_id=session_id
        )
        text_result = aai_request.aai_voice_to_text_request(voice_data)

        tbp_request = TbpRequest(
            bot_id=bot_id,
            secret_id=secret_id,
            secret_key=secret_key,
            session_id=session_id,
            text=text_result or '你好'
        )
        resp_text = tbp_request.tbp_request()
        voice_result = aai_request.aai_text_to_voice_request(resp_text)

        self.write({
            'Result': voice_result
        })


class VoiceToTextHandler(tornado.web.RequestHandler):
    """
    输入语音，输出文字
    """

    def data_received(self, chunk):
        pass

    def get(self):
        pass

    def post(self, *args, **kwargs):
        session_id = self.get_argument('session_id')
        voice_data = self.get_argument('voice_data')

        bot_id = "f8af9c03-bf86-4d45-a571-93dd3af8fda0"
        secret_id = 'AKIDf5IHsMxeS4ScZGkFwQgkcHl7E7lZLTZO'
        secret_key = 'knlTvAlPofIiuqa5RYimeGdsrdqrfmgO'

        aai_request = AaiRequest(
            secret_id=secret_id,
            secret_key=secret_key,
            session_id=session_id
        )
        text_result = aai_request.aai_voice_to_text_request(voice_data)

        tbp_request = TbpRequest(
            bot_id=bot_id,
            secret_id=secret_id,
            secret_key=secret_key,
            session_id=session_id,
            text=text_result or '你好'
        )
        resp_text = tbp_request.tbp_request()

        self.write({
            'Result': resp_text
        })


class TextToTextHandler(tornado.web.RequestHandler):
    """
    文字转文字
    """

    def data_received(self, chunk):
        pass

    def get(self):
        pass

    def post(self, *args, **kwargs):
        session_id = self.get_argument('session_id')
        text_data = self.get_argument('text_data')

        bot_id = "f8af9c03-bf86-4d45-a571-93dd3af8fda0"
        secret_id = 'AKIDf5IHsMxeS4ScZGkFwQgkcHl7E7lZLTZO'
        secret_key = 'knlTvAlPofIiuqa5RYimeGdsrdqrfmgO'

        tbp_request = TbpRequest(
            bot_id=bot_id,
            secret_id=secret_id,
            secret_key=secret_key,
            session_id=session_id,
            text=text_data or '你好'
        )
        resp_text = tbp_request.tbp_request()
        logging.info(">>text-to-text:resp_test:{}".format(resp_text))
        self.write({
            'Result': resp_text
        })


class TextToVoiceHandler(tornado.web.RequestHandler):
    """
    文字转语音
    """

    def data_received(self, chunk):
        pass

    def get(self):
        pass

    def post(self, *args, **kwargs):
        session_id = self.get_argument('session_id')
        text_data = self.get_argument('text_data')

        bot_id = "f8af9c03-bf86-4d45-a571-93dd3af8fda0"
        secret_id = 'AKIDf5IHsMxeS4ScZGkFwQgkcHl7E7lZLTZO'
        secret_key = 'knlTvAlPofIiuqa5RYimeGdsrdqrfmgO'

        tbp_request = TbpRequest(
            bot_id=bot_id,
            secret_id=secret_id,
            secret_key=secret_key,
            session_id=session_id,
            text=text_data or '你好'
        )
        resp_text = tbp_request.tbp_request()

        aai_request = AaiRequest(
            secret_id=secret_id,
            secret_key=secret_key,
            session_id=session_id
        )
        voice_result = aai_request.aai_text_to_voice_request(resp_text)

        self.write({
            'Result': voice_result
        })
