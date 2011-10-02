#-*- coding: utf-8 -*-
__author__ = 'Vladimir Ignatyev'

import sys, Skype4Py
from config import Configuration
from drivers.skype import SkypeNotifier, SkypeSmsNotifier
from time import sleep
from core.watcher import HttpServerWatcher

skype = Skype4Py.Skype()  # create a Skype API instance
#if not skype.Client.IsRunning:
#    print "[ERROR] You must start Skype to use application."
#    exit(1)
#else:
#    skype.Attach()

skype.Attach()

watchers = []
config = Configuration().getData()

print "[STATUS] HTTP servers monitor starting..."

for i in config:
    if i == 'http':
        for url in config[i]:
            for m in config[i][url]:
                notifiersList = []
                if m == 'skype':
                    for account in config[i][url][m]:
                        notifiersList.append(SkypeNotifier(skype, account))
                elif m == 'skypeSms':
                    for account in config[i][url][m]:
                        notifiersList.append(SkypeSmsNotifier(skype, account))
                watchers.append(HttpServerWatcher(url, notifiersList))

print "[STATUS] HTTP servers monitor started."

while True:
    sleep(10)
