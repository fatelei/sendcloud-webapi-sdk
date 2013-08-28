#!/usr/bin/python
#-*-coding: utf8-*-

import gzip
import cStringIO


def compress_content(content):
    """
    compress the content to sending
    """
    out = cStringIO.StringIO()
    gzipfile = gzip.GzipFile(fileobj=out, mode='w', compresslevel=9)
    gzipfile.write(content)
    gzipfile.close()
    out.seek(0)
    byte = out.read(1)
    byteArr = []
    while byte:
        byteArr.append(byte)
        byte = out.read(1)
    return bytearray(byteArr).decode('iso-8859-s1')
