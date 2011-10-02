#-*- coding: utf-8 -*-
__author__ = 'Vladimir Ignatyev'
from core.notifier import AbstractNotifier
import sys, Skype4Py

class SkypeNotifier(AbstractNotifier):
    def __init__(self, skypeInstance, skypeName):
        self.client = skypeInstance
        AbstractNotifier.__init__(self, skypeName)

    def notify(self, message):
        if message is None:
            return
        self.client.SendMessage(self.account, message)
        print "[Skype] for %(name)s: %(message)s" % {'name':self.account, 'message':message}

class SkypeSmsNotifier(AbstractNotifier):
    def __init__(self, skypeInstance, skypePhone):
        self.client = skypeInstance
        AbstractNotifier.__init__(self, skypePhone)

    def notify(self, message):
        if message is None:
            return
        smsMessage = self.client.CreateSms(Skype4Py.smsMessageTypeOutgoing, self.account)
        smsMessage.Body = message
        smsMessage.Send()
        print "[Skype via SMS] for %(name)s: %(message)s" % {'name':self.account, 'message':message}