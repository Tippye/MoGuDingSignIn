import datetime
import json

import api
from utils import compute_sign, notice


class User:
    username = None
    password = None
    address = None
    country = None
    province = None
    city = None
    longitude = None
    latitude = None
    notice_key = None
    userId = None
    token = None
    planId = None
    sign = None
    week = None

    def __init__(self, tube):
        self.username = tube[0]
        self.password = tube[1]
        self.address = tube[2]
        self.country = tube[3]
        self.province = tube[4]
        self.city = tube[5]
        self.longitude = tube[6]
        self.latitude = tube[7]
        self.notice_key = tube[8]
        self.week = tube[9]

    def login(self):
        """
        登录

        :return: 
        """
        data = json.dumps({
            "password": self.password,
            "phone": self.username,
            "loginType": "android",
            "uuid": ""
        })

        temp_json = api.login(data)

        self.userId = temp_json["data"]["userId"]
        self.token = temp_json["data"]["token"]
        print(self.userId + "登录成功")

    def signin(self, state="START"):
        """
        签到

        :param state: 
        :return: 
        """
        self.get_planid()
        self.get_sign(state)
        sign_in_json = json.dumps({
            "country": self.country,
            "address": self.address,
            "province": self.province,
            "city": self.city,
            "latitude": self.latitude,
            "description": "",
            "planId": self.planId,
            "type": state,
            "device": "Android",
            "longitude": self.longitude
        })
        try:
            signin_return = api.signin(data=sign_in_json, token=self.token, sign=self.sign)
            if signin_return["msg"] == "success":
                print(self.username + "成功")
            else:
                print(signin_return["msg"])
                print(json.loads(signin_return)["msg"])
                print(self.username + "签到成功")
                notice(self.notice_key, "签到成功")
        except Exception as e:
            print("SignIn错误：\n\t")
            print(str(e))
            notice(self.notice_key, "签到失败，请到工学云手动签到")

    # def get_report_week(self):
    #     """
    #     获取周报情况
    #     :return:
    #     """
    #     self.get_planid()
    #     return api.get_report("week", self.planId, self.token)

    def sub_report(self, week, title, content, type="week"):
        """
        提交周报

        :param week: 周数
        :param title: 周报标题
        :param content: 周报内容
        :param type:
        :return:
        """
        self.get_planid()
        self.get_report_sign(title, type)
        today = datetime.datetime.today().date()
        json_str = "{\"reportType\":\"week\",\"address\":\"\",\"weeks\":\"第" + week + "周\",\"latitude\":\"0.0\"," + "\"planId\":\"" + self.planId + "\"," + "\"startTime\":\" " + (
                today - datetime.timedelta(days=today.weekday())).strftime(
            "%Y-%m-%d 00:00:00") + "\"," + "\"yearmonth\":\"\"," + "\"endTime\":\"" + (
                           today + datetime.timedelta(days=6 - today.weekday())).strftime(
            "%Y-%m-%d 23:59:59") + "\"," + "\"title\":\"" + title + "\"," + "\"content\":\"" + content + "\"," + "\"longitude\":\"0.0\"}"
        try:
            rep_res = api.sub_report(json_str, self.token, self.sign)
            print(rep_res)
            print(self.username + "周报上交成功")
            notice(self.notice_key, "周报提交成功，内容为:\n" + content)
        except Exception as e:
            print(e)
            print(self.username + "周报上交失败")
            notice(self.notice_key, "周报提交失败，请前往工学云手动提交")

    def get_planid(self):
        """
        获取planID

        :return:
        """
        sign = compute_sign(self.userId + "student3478cbbc33f84bd00d75d7dfa69e0daa")
        self.planId = api.get_planid(token=self.token, sign=sign)
        # print("planId = " + self.planId)

    def get_report_sign(self, title, type="week"):
        """
        获取周报签名

        :param title: 周报标题
        :param type: 周报类型
        :return:
        """
        _str = self.userId + type + self.planId + title + "3478cbbc33f84bd00d75d7dfa69e0daa"
        try:
            self.sign = compute_sign(_str)
            print("sign = " + self.sign)
        except Exception as e:
            print("getReportSign错误：\n\t")
            print(e)

    def get_sign(self, state="START"):
        """
        获取签到签名

        :param state:签到类型。START/END
        :return:
        """
        _str = "Android" + state + self.planId + self.userId + self.address + "3478cbbc33f84bd00d75d7dfa69e0daa"
        try:
            self.sign = compute_sign(_str)
            # print("sign = " + self.sign)
        except Exception as e:
            print("getSign错误：\n\t")
            print(e)
