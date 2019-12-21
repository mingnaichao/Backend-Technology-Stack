# -*- coding: utf-8 -*-
# @author : mingnaichao
# @date : 2019/10/6
# @time : 15:12
import binascii
import hashlib
import hmac
import json
import random
import sys
import time
from urllib.request import quote


def aai_text_to_voice_url_params(secret_id, secret_key, session_id, text):
    """
    文字转语音url参数
    :param secret_id:
    :param secret_key:
    :param session_id:
    :param text:
    :return:
    """
    param = {
        "Nonce": random.randint(1, sys.maxsize),
        "Timestamp": int(time.time()),
        "Region": "ap-guangzhou",
        "SecretId": secret_id,
        "Action": "TextToVoice",
        "Version": "2018-05-22",
        "SessionId": session_id,
        "Volume": "0",
        "Speed": "1",
        "ProjectId": "0",
        "ModelType": "1",
        "VoiceType": "0",
        "PrimaryLanguage": "1",
        "SampleRate": "8000",
        "Codec": "wav",
        "Text": text
    }

    # 生成待签名字符串
    sign_str = "GETaai.tencentcloudapi.com/?"
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


def aai_voice_to_text_url_params(secret_id, secret_key, session_id, voice_data):
    """
    语音转文字url参数
    :param secret_id:
    :param secret_key:
    :param session_id:
    :param voice_data:
    :return:
    """
    param = {
        "Nonce": random.randint(1, sys.maxsize),
        "Timestamp": int(time.time()),
        "Region": "ap-guangzhou",
        "SecretId": secret_id,
        "Action": "SentenceRecognition",
        "Version": "2018-05-22",
        "ProjectId": "0",
        "SubServiceType": "2",
        "EngSerViceType": "8k",
        "SourceType": "1",
        "VoiceFormat": "wav",
        "UsrAudioKey": session_id
    }

    # 生成待签名字符串
    sign_str = "GETaai.tencentcloudapi.com/?"
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
    # fwave = open('./test.wav', mode='r')
    # data = str(fwave.read())
    # param['DataLen'] = len(data)
    # param['Data'] = base64.b64encode(data)

    new_voice_data = ''
    for _string in str(voice_data):
        new_voice_data += '+' if _string == ' ' else _string  # 将空字符用加号代替
    param['Data'] = new_voice_data
    new_voice_data.decode('base64')
    param['DataLen'] = len(new_voice_data)

    return json.dumps(param)
