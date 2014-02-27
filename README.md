url2android
===========

Open a computer URL in the clipboard URL ( PC ) in android.

This script receives a URL from the computer through the
http protocol in port 8080 and opens it in the Android Browser.
It runs in the Android with sl4a script layer
in the Android python interpreter.

Credits: Marcel Hellkamp, without python bottle module it wouldn't be possible.

# Files

1. url2android_receiver.py  -- Bottle web server that runs android.
2. bottle.py -- Python bottle web server
3. url2android_sender.py  -- Sends the URL to server running in the android.

# Installation

###### Android Device

1. Install sl4a script layer and python for android
2. Move url2android_receiver.py and bottle.py to  /sdcard/sl4a/receiver
3. Run the script url2android_receiver.py in the android device.


###### Computer

1. Copy the url2android_sender.py ( modify the android IP) to the PC.

2. Open the URL http://android-ip:8080 and enter the URL that will be opened
   in android

3. Copy the link and run  url2android_sender.py to open the url in the android browser.

