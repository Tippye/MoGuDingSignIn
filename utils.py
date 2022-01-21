import hashlib

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


def computeSign(str):
    md = hashlib.md5()
    md.update(bytes(str, encoding="utf8"))
    return md.hexdigest()
