#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
url2android_receiver.py

This script receives the URL through the http protocol
in port 8080. It runs in the Android with sl4a script layer
in the Android python interpreter.

To receive the URL.
Enter in the browser: http://android-ip:8080 and enter the URL in
the PC Browser, then it will open in the Android device.

Other way to send the URL is copy the URL in the computer and
execute the script  url2android_sender.py.

Tip: add a fixed IP to android.

"""

__author__ = "Caio Rodrigues"

from bottle import route, request, run, template,validate, static_file
from multiprocessing import Process

import android

droid = android.Android()

def showurl(url="http://localhost:8080"):
    #time.sleep(5)
    droid.webViewShow(url)



@route('/url')
def  go_url():

    url_form = '''
    <br />
    <form action="/url" method="GET">
            Browser to Android URL <br /><input name="q" type="text" autofocus />
            <input value="GO" type="submit" />
        </form>
    '''

    url = request.params.get('q')
#    droid.webViewShow(url)
    droid.startActivity('android.intent.action.VIEW', url)

    return  url_form

@route('/')
def home_page():

    url_form = '''
    <br />
    <form action="/url" method="GET">
            Search Library <br /><input name="q" type="text" autofocus />
            <input value="Search" type="submit" />
        </form>
    '''

    return url_form

#p=Process(target=showurl)
#p.start()
run(host='0.0.0.0', port=8080)



