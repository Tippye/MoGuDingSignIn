import pymysql

from User import User
import api
from config import DatabasePath, DatabaseUser, DatabasePwd, Database, dev

if __name__ == "__main__":
    connection = None

    try:
        users = api.get_users()
        connection = pymysql.connect(host=DatabasePath, user=DatabaseUser, password=DatabasePwd, db=Database,
                                     charset="utf8mb4")
        cursor = connection.cursor()
        for user_data in users:
            user = User(user_data)
            if user.week > -1:
                # 查询上周提交的周报
                sql = "SELECT report_id FROM week_report_log WHERE username=" + user.username
                cursor.execute(sql)
                res = cursor.fetchone()
                title = ""
                content = ""
                if res and len(res) > 0:
                    print("上周提交过周报")
                    last_report_id = res[0]
                    # 查询本周周报
                    sql = "SELECT title,content FROM week_report WHERE id=(SELECT id FROM week_report WHERE week=" + str(
                        user.week + 1) + " AND series = (SELECT series FROM week_report WHERE id = " + str(
                        last_report_id) + "))"
                    cursor.execute(sql)
                    res = cursor.fetchone()
                    if res:
                        # 存在下一周的周报
                        title = res[0]
                        content = res[1]

                if content == "":
                    sql = "SELECT title,content FROM week_report LEFT JOIN week_report_log ON week_report.id=week_report_log.report_id WHERE type=0 AND week_report.week=" + str(
                        user.week + 1) + " AND (week_report_log.username<>" + str(
                        user.username) + " OR week_report_log.username IS NULL)"
                    cursor.execute(sql)
                    res = cursor.fetchone()
                    title = res[0]
                    content = res[1]
                if title is None:
                    title = "第" + str(user.week + 1) + "周"
                print("提交周报：\n\t标题：" + title + "\n\t内容：" + content)
                user.sub_report(user.week + 1, title, content)
    except Exception as e:
        print("数据库出现错误：")
        print("\t" + str(e))
    finally:
        connection.close()
