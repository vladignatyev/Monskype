#-*- coding: utf-8 -*-
__author__ = 'Vladimir Ignatyev'

class AbstractNotifier(object):
    def __init__(self, accountToNotify):
        self.account = accountToNotify
        return
    def notify(self, message):
        return

