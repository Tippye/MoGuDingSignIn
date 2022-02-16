import hashlib

import pymysql

from config import *

base = [str(x) for x in range(10)] + [chr(x) for x in range(ord('A'), ord('A') + 6)]


def dec2hex(string_num):
    """
    十进制转十六进制
    :param string_num: 十进制数
    :return:
    """
    num = int(string_num)
    mid = []
    while True:
        if num == 0: break
        num, rem = divmod(num, 16)
        mid.append(base[rem])
    result = ''.join([str(x) for x in mid[::-1]])
    return result


def compute_sign(str):
    """
    计算签名
    :param str:
    :return:
    """
    md = hashlib.md5()
    md.update(bytes(str, encoding="utf8"))
    return md.hexdigest()


def get_users():
    """
    从数据库获取用户信息
    :return:
    """
    connection = None

    try:
        connection = pymysql.connect(host=DatabasePath, user=DatabaseUser, password=DatabasePwd, db=Database,
                                     charset="utf8mb4")
        cursor = connection.cursor()
        sql = "SELECT * FROM user"
        cursor.execute(sql)

        return cursor.fetchall()
    except Exception as e:
        print("链接数据库出现错误：")
        print("\t" + str(e))
        return None


def err_notice():
    pass
