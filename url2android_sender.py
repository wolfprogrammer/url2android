#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
url2android_sender.py

This script sends the url in the clipboard ( PC running Linux )
to the Tablet running the server ( url2android_receiver.py )

"""
__author__ = 'Caio Rodrigues'

import os
from urllib2 import urlopen, quote

#---- Android IP --------------#
host = 'http://192.168.1.5:8080'

url = os.popen('xclip -selection clipboard -o').read()
#url  = quote(url)

print "url1 ", url

url = url.replace(' ', '%20')
url = url.replace('/', '%2F')
url = url.replace(':', '%3A')
url = url.replace(':', '%3A')
url = url.replace('#', '%23')
url = url.replace('+', '%3D')

url_ = "".join([host, "/url?q=", url])

print url_

data = urlopen(url_)


