from User import User
from utils import get_users

if __name__ == '__main__':
    # TODO: 请求500
    users = get_users()

    for u in users:
        user = User(u)
        user.login()
        temp_json = user.get_report_week()
        print(temp_json["data"])