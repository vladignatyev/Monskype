#-*- coding: utf-8 -*-
__author__ = 'Vladimir Ignatyev'

from httplib import HTTPConnection
from threading import Timer
from urlparse import urlparse

# Base class for all server watchers

class AbstractServerWatcher(object):
    STATE_UP = "up"
    STATE_DOWN = "down"

    def __init__(self, serverUrl, notifiersList,
                 serverDownMessage = "[notification] Server %(url)s is down! Http error code: %(error)s",
                 serverUpMessage = "[notification] Server %(url)s alive.",
                 timeout = 5):
        
        self.url = serverUrl
        self.notifiersList = notifiersList
        self.timeout = timeout
        self.serverDownMessage = serverDownMessage
        self.serverUpMessage = serverUpMessage
        self.serverState = ""
        self.timer = Timer(timeout, self.updateServerState)
        self.timer.start()
        self.updateServerState()
        return

    def updateServerState(self):
        self.timer = Timer(self.timeout, self.updateServerState)
        self.timer.start()
        return

    def notifyUsers(self, notifiersList, message):
        for notifier in notifiersList:
            notifier.notify(message)

    def setServerState(self, state, status):
        if state == self.serverState:
            return
        self.serverState = state
        if state == AbstractServerWatcher.STATE_UP:
            self.notifyUsers(self.notifiersList, self.serverUpMessage % { 'url': self.url, 'error': status })
        elif state == AbstractServerWatcher.STATE_DOWN:
            self.notifyUsers(self.notifiersList, self.serverDownMessage % { 'url': self.url, 'error': status })

class HttpServerWatcher(AbstractServerWatcher):
    def updateServerState(self):
        urlChunks = urlparse(self.url)
        connection = HTTPConnection(urlChunks.hostname, urlChunks.port)
        connection.request("GET", urlChunks.path)
        response = connection.getresponse()
        if response.status >= 400:
            self.setServerState(AbstractServerWatcher.STATE_DOWN, response.status)
        else:
            self.setServerState(AbstractServerWatcher.STATE_UP, response.status)

        AbstractServerWatcher.updateServerState(self)
