#!/usr/bin/python
#-*-coding: utf8-*-

from sendclound import SendCloud


if __name__ == "__main__":
    sc = SendCloud()
    kwargs = {"api_user": "api_user",
              "api_key": "api_key",
              "to": "receiver@foo.bar",
              "subject": "test",
              "from": "from@foo.bar",
              "fromname": "test",
              "html": "<p>Hello World</p>"}
    print sc.work("mailsend", **kwargs)