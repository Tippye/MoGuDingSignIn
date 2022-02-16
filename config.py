from urlobject import URLObject

# 数据库配置
DatabasePath = "47.105.183.120"
DatabaseUser = "moguding"
DatabasePwd = "2XcTdSR6CirJYHfd"
Database = "moguding"

# 接口地址
loginURL = URLObject("https://api.moguding.net:9000/session/user/v1/login")
signInURL = URLObject("https://api.moguding.net:9000/attendence/clock/v2/save")
planIdURL = URLObject("https://api.moguding.net:9000/practice/plan/v3/getPlanByStu")
weekReportURL = URLObject("https://api.moguding.net:9000/practice/paper/v2/save")
weekReportListURL = URLObject("https://api.moguding.net:9000/practice/paper/v2/listByStu")
# monthReportURL = URLObject("")

# http请求头部信息。
Accept_Language = "zh-CN,zh;q=0.8"
user_agent_value = "Mozilla/5.0 (Linux; Android 7.0; HTC M9e Build/EZG0TF) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.1566.54 Mobile Safari/537.36"
Content_Type = "application/json; charset=UTF-8"
Host = "api.moguding.net:9000"
Accept_Encoding = ""
Cache_Control = "no-cache"

# SMTP
mailServer = "smtp.163.com"
mailPort = 465
mailAccount = "Tippy_q@163.com"
mailPassword = "DZYCFELLNVXOYIKF"
mailSender = "Tippy"
