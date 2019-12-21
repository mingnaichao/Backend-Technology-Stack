# -*- coding: utf-8 -*-
# @author : mingnaichao
# @date : 2019/10/2
# @time : 15:01

from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.tbp.v20190627 import tbp_client, models

from tbp_params import tbp_url_params


class TbpRequest(object):
    """
    智能会话请求
    """

    def __init__(self, bot_id, secret_id, secret_key, session_id, text, bot_env=None):
        self.bot_id = bot_id
        self.secret_id = secret_id
        self.secret_key = secret_key
        self.session_id = session_id
        self.text = text
        self.bot_env = bot_env

    def tbp_request(self):
        """
        发起会话请求
        :return:
        """
        try:
            cred = credential.Credential(self.secret_id, self.secret_key)
            http_profile = HttpProfile()
            http_profile.endpoint = "tbp.tencentcloudapi.com"

            client_profile = ClientProfile()
            client_profile.httpProfile = http_profile
            client = tbp_client.TbpClient(cred, "ap-guangzhou", client_profile)

            req = models.TextProcessRequest()
            params = tbp_url_params(
                self.bot_id, self.secret_id, self.secret_key, self.session_id, self.text, self.bot_env
            )
            req.from_json_string(params)
            resp = client.TextProcess(req)
            # print resp.to_json_string()
            for group_message in resp.ResponseMessage.GroupList:
                return group_message.Content

        except TencentCloudSDKException as err:
            print(err)
