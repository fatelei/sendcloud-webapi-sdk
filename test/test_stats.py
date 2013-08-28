#!/usr/bin/python
#-*-coding: utf8-*-

from sendcloud import SendCloud

if __name__ == "__main__":
    sc = SendCloud()
    kwargs = {"api_user": "api_user",
              "api_key": "api_key",
              "days": 20}
    print sc.work("mailstats", **kwargs)
