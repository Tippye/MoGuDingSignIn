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
    TempJson = None
    userId = None
    token = None
    planId = None
    sign = None

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
