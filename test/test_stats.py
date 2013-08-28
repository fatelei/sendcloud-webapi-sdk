#!/usr/bin/python
#-*-coding: utf8-*-

from sendcloud import SendCloud

if __name__ == "__main__":
    sc = SendCloud()
    kwargs = {"api_user": "postmaster@newsletter2.zhihu.com",
              "api_key": "F3LJNCXt",
              "days": 20}
    print sc.work("mailstats", **kwargs)
