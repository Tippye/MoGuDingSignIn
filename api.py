import json

import requests

from config import *


def post_request(url, json_str, token="", sign="", role_key=""):
    """
    发送请求
    :param url:
    :param json_str:
    :param token:
    :param sign:
    :param role_key:
    :return:
    """
    try:
        headers = {
            "User-Agent": user_agent_value,
            "Content-Type": Content_Type,
            "Host": Host,
            "Accept-Language": Accept_Language,
            "Sign": sign,
            "Authorization": token,
            "roleKey": role_key,
            "Accept-Encoding": Accept_Encoding,
            "Cache-Control": Cache_Control
        }
        return json.loads(requests.request("post", url=url, headers=headers, data=json_str).text)
    except ConnectionError:
        print("网络连接失败")
    except Exception as e:
        print(e)


def login(data):
    return post_request(url=loginURL, json_str=data)


def get_planid(token, sign):
    return post_request(url=planIdURL, json_str="{\"state\":\"\"}", token=token, sign=sign,
                        role_key="student")["data"][0]["planId"]


def signin(data, token, sign):
    return post_request(url=signInURL, json_str=data, token=token, sign=sign, role_key="student")


def get_report(type, planid, token):
    json_str = json.dumps({
        "currPage": 1,
        "reportType": type,
        "pageSize": 20,
        "planId": planid
    })
    return post_request(url=weekReportListURL, json_str=json_str, token=token)


def sub_report(json_str, token, sign):
    return post_request(url=weekReportURL, json_str=json_str, token=token, role_key="student", sign=sign)
