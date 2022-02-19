import hashlib
import re

from mail import send_mail

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


def notice(notice, content):
    """
    通知
    :param notice:
    :param content:
    :return:
    """
    if notice is None:
        return
    mail_str = r'^[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}$'
    if re.match(mail_str, notice):
        send_mail(content, "工学云签到错误", "Tippy_q@163.com", notice, notice)
