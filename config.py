#-*- coding: utf-8 -*-

class Configuration(object):
    def __init__(self):
        return

    def getData(self):
        return \
            {
            'http':
                    {
                    "http://url.com:8000/":
                            {'skype':["user.name1", "user.name2"]},
							
                    "http://url2.com:80/":
                            {'skype':["user.name3"], 'skypeSms':["+12345678910"]},
                }
        }

