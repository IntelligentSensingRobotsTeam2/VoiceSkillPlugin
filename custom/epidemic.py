# -*- coding: utf-8-*-
# author: 41
# 疫情咨询
import requests
import json
from robot.sdk import unit
from robot import config, logging
from robot.sdk.AbstractPlugin import AbstractPlugin

logger = logging.getLogger(__name__)

class Plugin(AbstractPlugin):

    SLUG = "epidemic"

    def handle(self, text, parsed):
        # get config
        sentense = unit.getSay(parsed)[:-8]
        
        self.say(sentense)


    def isValid(self, text, parsed):
        # print(parsed['result']['response_list'])
        return unit.hasIntent(parsed,'BUILT_EPIDEMIC')
                


