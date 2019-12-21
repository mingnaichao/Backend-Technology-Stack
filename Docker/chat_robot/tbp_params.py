# -*- coding: utf-8 -*-
# @author : mingnaichao
# @date : 2019/10/2
# @time : 14:29
import binascii
import hashlib
import hmac
import json
import random
import sys
import time
from urllib.request import quote


def tbp_url_params(bot_id, secret_id, secret_key, session_id, input_text, bot_env=None):
    """
    url参数
    :param bot_id:
    :param secret_id:
    :param secret_key:
    :param session_id:
    :param input_text:
    :param bot_env:
    :return:
    """
    param = {
        "Nonce": random.randint(1, sys.maxsize),
        "Timestamp": int(time.time()),
        "Region": "ap-guangzhou",
        "SecretId": secret_id,
        "Action": "TextProcess",
        "Version": "2019-06-27",
        "BotId": bot_id,
        "BotEnv": bot_env or "dev",
        "TerminalId": session_id,
        'InputText': input_text
    }

    # 生成待签名字符串
    sign_str = "GETtbp.tencentcloudapi.com/?"
    sign_str += "&".join("%s=%s" % (k, param[k]) for k in sorted(param))

    # 生成签名
    if sys.version_info[0] > 2:
        sign_str = bytes(sign_str, "utf-8")
        secret_key = bytes(secret_key, "utf-8")

    hashed = hmac.new(secret_key, sign_str, hashlib.sha1)
    signature = binascii.b2a_base64(hashed.digest())[:-1]

    if sys.version_info[0] > 2:
        signature = signature.decode()

    param['Signature'] = quote(signature)

    return json.dumps(param)
