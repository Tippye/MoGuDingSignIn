from User import User

if __name__ == '__main__':
    # user = User(("19819793086", "Qwe123456", "滕州市荆河街道河阳路", "中国", "山东省", "枣庄市", "117.154", "35.0797",""))
    user = User(("19853149246", "AM99791128y", "龙湖区珠池街道广兴街", "中国", "广东省", "汕头市", "116.741", "23.3691", ""))
    user.login()
    temp_json = user.sub_report(1, "第一周周报",
                               "时间就像一个永不停息的机器，转眼间大学二年即将结束。在完成大学生涯前，等着我们的还有一门必修课去完成----实习。一个星期过去了，虽然还没怎么适应这里的环境不过这里的人还是比较开朗友善的，他们渐渐的把我拉入这里的氛围里面了。一开始怕融入不了这个环境的念头给打消了。工作之余他们给我讲述了不少公司里人际处理的方法，讲述了些公司年会的举办及进程等，对于我来说尤其 能那么快适应真的非常的重要。同时向我介绍了一下公司的基本情况，比如发展历史，人员数量，产品的卖点等等。还有公司的基本制度比如：上班时间，下班时间，节假日的放假情况等。已级公司的组成，有好几个不同职能的小车间组成的而我主要是先被分配到了验整上。和公司的业余安排等，每个星期的一三五晚上有最新的电影免费在二楼的食堂播放等。\n工作的地点也去看过了，迷迷糊糊之间，一个星期过去了。使我对公司的基本情况有了一个初步的认识和基本的了解。同时一周下来，也给我很多感触，体会到了一些在校园，在学生时期无法体会到的东西。\n同时还从领导身上学到了很多关于工作的经验和基础知识。这对我而言都是十分宝贵的收获了。但作为一名员工而言，我其实还并不太适应这里的环境。比起学校，在工作岗位上要更加的严肃且严谨。虽然对工作我充满了热情，但也十分怕因为自己的不小心给大家带来麻烦。总之，虽然还有不少需要解决的问题，但我已经在这周开始渐渐适应这个新的环境和工作，相信在后面我一定会有更好的表现！")
    print(temp_json)
