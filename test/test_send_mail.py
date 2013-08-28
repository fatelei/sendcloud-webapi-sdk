#!/usr/bin/python
#-*-coding: utf8-*-

from sendclound import SendCloud


if __name__ == "__main__":
    sc = SendCloud()
    kwargs = {"api_user": "postmaster@newsletter2.zhihu.com",
              "api_key": "F3LJNCXt",
              "to": "1443343615@qq.com",
              "subject": "test",
              "from": "fatelei@gmail.com",
              "fromname": "test",
              "html": "<p>Hello World</p>"}
    print sc.work("mailsend", **kwargs)