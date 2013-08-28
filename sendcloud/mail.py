#!/usr/bin/python
#-*-coding: utf8-*-

"""
SendCloud API for mail send
"""

import requests
import json

from message import Message


class SendCloud(object):

    def __init__(self):
        self.func_map = {
            "mailsend": "self.mail_send",
            "mailstats": "self.mail_stats"
        }

    def work(self, work_type, **kwargs):
        if work_type not in self.func_map:
            raise KeyError(u"unknown work type: %s" % work_type)
        else:
            return eval(self.func_map[work_type])(**kwargs)

    def decode_json(self, json_data):
        """
        decode json data
        """
        try:
            data = json.loads(json_data)
            return data
        except:
            raise ValueError(u"not a json object")

    def mail_send(self, **kwargs):
        """
        send mail
        """
        msg = Message()
        data = msg.generate_mail_msg(**kwargs)
        resp = requests.post(
            "https://sendcloud.sohu.com/webapi/mail.send.json", data)

        rst = self.decode_json(resp.text)

        if rst["message"] == "success":
            return "send mail successfully!"
        else:
            return "send mail failed: %s" % rst["errors"][0]


    def mail_stats(self, **kwargs):
        """
        get mail stats
        """
        msg = Message()
        data = msg.generate_stats_msg(**kwargs)
        resp = requests.post("https://sendcloud.sohu.com/webapi/stats.get.json", data)

        rst = self.decode_json(resp.text)

        if rst["message"] == "success":
            return rst["stats"]
        else:
            return "get mail's stats failed: %s" % rst["errors"][0]