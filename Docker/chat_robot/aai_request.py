# -*- coding: utf-8 -*-
# @author : mingnaichao
# @date : 2019/10/6
# @time : 15:12
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.aai.v20180522 import aai_client, models

from aai_params import aai_text_to_voice_url_params, aai_voice_to_text_url_params


class AaiRequest(object):
    """
    语音合成
    """

    def __init__(self, secret_id, secret_key, session_id):
        self.secret_id = secret_id
        self.secret_key = secret_key
        self.session_id = session_id

    def aai_text_to_voice_request(self, text):
        """
        文字转语音
        :param text: 智能会话返回的文本
        :return:
        """
        try:
            cred = credential.Credential(self.secret_id, self.secret_key)
            http_profile = HttpProfile()
            http_profile.endpoint = "aai.tencentcloudapi.com"

            client_profile = ClientProfile()
            client_profile.httpProfile = http_profile
            client = aai_client.AaiClient(cred, "ap-guangzhou", client_profile)

            req = models.TextToVoiceRequest()
            params = aai_text_to_voice_url_params(self.secret_id, self.secret_key, self.session_id, text)
            req.from_json_string(params)

            resp = client.TextToVoice(req)
            return resp.Audio

        except TencentCloudSDKException as err:
            print(err)

    def aai_voice_to_text_request(self, voice_data):
        """
        语音转文字
        :param voice_data:
        :return:
        """
        try:
            cred = credential.Credential(self.secret_id, self.secret_key)
            http_profile = HttpProfile()
            http_profile.endpoint = "aai.tencentcloudapi.com"

            client_profile = ClientProfile()
            client_profile.httpProfile = http_profile
            client = aai_client.AaiClient(cred, "ap-guangzhou", client_profile)

            req = models.SentenceRecognitionRequest()
            params = aai_voice_to_text_url_params(self.secret_id, self.secret_key, self.session_id, voice_data)
            req.from_json_string(params)

            resp = client.SentenceRecognition(req)

            return resp.Result

        except TencentCloudSDKException as err:
            print(err)
