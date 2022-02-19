from User import User
from api import get_users

if __name__ == "__main__":
    users = get_users()
    for u in users:
        user = User(u)
        user.login()
        user.signin()
