# import json
# import time
#
# import requests
# from urlobject import URLObject
# import pymysql.cursors
#
# from User import User
# from config import *
# from utils import computeSign
#
# # 上班/下班 START/END
# State = "START"
#
# # 初始化数据
# day = 0
#
#
# def init():
#     global day
#     day = int(time.strftime("%d", time.localtime()))
#
#
# def PostRequest(url, json_str, token="", sign="", role_key=""):
#     """
#     发送请求
#     :param url:
#     :param json_str:
#     :param token:
#     :param sign:
#     :param role_key:
#     :return:
#     """
#     try:
#         headers = {
#             "User-Agent": user_agent_value,
#             "Content-Type": Content_Type,
#             "Host": Host,
#             "Accept-Language": Accept_Language,
#             "Sign": sign,
#             "Authorization": token,
#             "roleKey": role_key,
#             "Accept-Encoding": Accept_Encoding,
#             "Cache-Control": Cache_Control
#         }
#         return json.loads(requests.request("post", url=url, headers=headers, data=json_str).text)
#     except ConnectionError:
#         print("网络连接失败")
#     except Exception as e:
#         print(e)
#
#
# def getUserId(_user):
#     """
#     获取userId
#     :return:
#     """
#     _user.userId = _user.TempJson["data"]["userId"]
#     print("UserID = " + _user.userId + "\n")
#
#
# def getToken(_user):
#     """
#     获取token
#     :return:
#     """
#     _user.token = _user.TempJson["data"]["token"]
#     print("token = " + _user.token + "\n")
#
#
# def getPlanIdSign(_user):
#     """
#     获取任务签名
#     """
#     _str = _user.userId + "student3478cbbc33f84bd00d75d7dfa69e0daa"
#     try:
#         _user.sign = computeSign(_str)
#         print("PlanID = " + _user.sign)
#     except Exception as e:
#         print("getPlanIdSign")
#         print(e)
#
#
# def getPlanId(_user):
#     _user.TempJson = PostRequest(url=planIdURL, json_str="{\"state\":\"\"}", token=_user.token, sign=_user.sign,
#                                  role_key="student")
#     _user.planId = _user.TempJson['data'][0]['planId']
#     print("planId = " + _user.planId)
#
#
# def getSign(_user):
#     _str = "Android" + State + _user.planId + _user.userId + _user.address + "3478cbbc33f84bd00d75d7dfa69e0daa"
#     try:
#         _user.sign = computeSign(_str)
#         print("sign = " + _user.sign)
#     except Exception as e:
#         print("getSign")
#         print(e)
#
#
# def signin(_user):
#     try:
#         data = json.dumps({
#             "password": _user.password,
#             "phone": _user.username,
#             "loginType": "android",
#             "uuid": ""
#         })
#
#         _user.TempJson = PostRequest(url=loginURL, json_str=data)
#         getUserId(_user)
#         getToken(_user)
#         getPlanIdSign(_user)
#
#         getPlanId(_user)
#
#         getSign(_user)
#
#         sign_in_json = json.dumps({
#             "country": _user.country,
#             "address": _user.address,
#             "province": _user.province,
#             "city": _user.city,
#             "latitude": _user.latitude,
#             "description": "",
#             "planId": _user.planId,
#             "type": State,
#             "device": "Android",
#             "longitude": _user.longitude
#         })
#
#         try:
#             login_return = PostRequest(url=signInURL, json_str=sign_in_json, token=_user.token, sign=_user.sign,
#                                        role_key="student")
#             print(login_return)
#             print(_user.username + "签到成功")
#         except Exception as e:
#             print("SignIn")
#             print(str(e))
#             if _user.notice_key:
#                 requests.request("get", url="https://sc.ftqq.com/" + _user.notice_key + ".send?text=签到失败，请手动签到")
#     except Exception as e:
#         print(e)
#         if _user.notice_key:
#             requests.request("get", url="https://sc.ftqq.com/" + _user.notice_key + ".send?text=签到失败，请手动签到")
#         print(_user.username + " 签到失败")
#
#
# if __name__ == '__main__':
#     init()
#
#     # bf_in = None
#     connection = None
#
#     try:
#         connection = pymysql.connect(host=DatabasePath, user=DatabaseUser, password=DatabasePwd, db=Database,
#                                      charset="utf8mb4")
#         cursor = connection.cursor()
#         sql = "SELECT * FROM user"
#         cursor.execute(sql)
#
#         result = cursor.fetchall()
#
#         for (u) in result:
#             print("#" * 50)
#             user = User(u)
#             signin(user)
#             print("#" * 50)
#
#     except IOError:
#         print("Error:IO error")
#     finally:
#         connection.close()
