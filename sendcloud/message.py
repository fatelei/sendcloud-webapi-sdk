#!/usr/bin/python
#-*-coding: utf8-*-

"""
sendcloud webapi parameters
"""

import re

from utils import compress_content


class Message(object):

    def __init__(self):
        self.email_regex = re.compile(
            r"^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$")
        self.date_regex = re.compile(r"^\d{4}-\d{2}-\d{2}$")

    def check_valid(self, key, data, _type):
        """
        check the data type
        """
        if not isinstance(data[key], _type):
            raise ValueError(u"not a valid data: key: %s" % key)

    def check_email_valid(self, email):
        """
        check whether email is valid
        """
        emails_list = email.split(":")
        check_func = lambda x: self.email_regex.match(x)
        reduce_func = lambda x, y: x and y

        is_valid = reduce(reduce_func, map(check_func, emails_list))
        if is_valid:
            return True
        else:
            raise Exception(u"invalid email address")

    def generate_mail_msg(self, **kwargs):
        """
        generate parameters for sending mail

        kwargs:
            to: the receivers, type is str, the format is: foo@bar.com:foo1@bar1.com
            subject: the theme of email
            html: the content of email
            from: the sender's mail address
            fromname: the sender's name, optional
            cc: cc recipients, accept list type, optional
            bcc: bcc recipients, accept list type, optional
            headers: add headers to message, accept dict type, optional
            replyto: the address of reply, optional
            gzip_compress: send compressed content, optional
        """

        if "to" not in kwargs:
            raise Exception(u"parameters error: no to")
        self.check_valid("to", kwargs, str)
        self.check_email_valid(kwargs["to"])

        if "subject" not in kwargs:
            raise Exception(u"parameters error: no subject")
        self.check_valid("subject", kwargs, str)

        if "html" not in kwargs:
            raise Exception(u"parameters error: no html")
        self.check_valid("subject", kwargs, str)

        if "fromname" in kwargs and len(kwargs["fromname"]) == 0:
            raise Exception(u"parameters error: fromname can't be empty")
        self.check_valid("fromname", kwargs, str)

        self.check_email_valid(kwargs["from"])

        if "cc" in kwargs:
            self.check_valid("cc", kwargs, str)
            self.check_email_valid(kwargs["cc"])

        if "bcc" in kwargs:
            self.check_valid("bcc", kwargs, str)
            self.check_email_valid(kwargs["bcc"])

        if "replyto" in kwargs:
            self.check_email_valid(kwargs["replyto"])

        if "headers" in kwargs:
            self.check_valid("headers", kwargs, dict)

        if "gzip_compress" in kwargs:
            self.check_valid("gzip_compress", kwargs, bool)
            kwargs["gzip_compress"] = int(kwargs["gzip_compress"])
            if kwargs["gzip_compress"]:
                kwargs["content"] = compress_content(kwargs["content"])

        return kwargs


    def generate_stats_msg(self, **kwargs):
        """
        generate parameters for getting stats

        kwargs:
            days: must be larger than 0, optional
            start_date: its format must be yyyy-MM-dd, optional
            end_date: its format must be yyyy-MM-dd, optional
            list: get categories if its valus is true, optional
            category: set specific category to get relate data, optional
        """

        if "days" in kwargs:
            self.check_valid("days", kwargs, int)
            if kwargs["days"] < 0:
                raise ValueError(u"days must be larger than 0")

        if "start_date" in kwargs:
            self.check_valid("start_date", kwargs, str)
            if not self.date_regex.match(kwargs["start_date"]):
                raise ValueError(u"start_date format must be yyyy-mm-dd")

        if "end_date" in kwargs:
            self.check_valid("end_date", kwargs, str)
            if not self.date_regex(kwargs["end_date"]):
                raise ValueError(u"end_date format must be yyyy-mm-dd")

        if "list" in kwargs:
            self.check_valid("list", kwargs, bool)
            kwargs["list"] = str(kwargs["list"]).lower()

        if "category" in kwargs:
            self.check_valid("category", kwargs, str)

        kwargs["aggregate"] = 1

        return kwargs
