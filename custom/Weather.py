# -*- coding: utf-8-*-
# 天气插件
import requests
import json
from robot.sdk import unit
from robot import config, logging
from robot.sdk.AbstractPlugin import AbstractPlugin

logger = logging.getLogger(__name__)

class Plugin(AbstractPlugin):

    SLUG = "weather"

    def handle(self, text, parsed):
        # get config
        self.say(unit.getSay(parsed))


    def isValid(self, text, parsed):
        keywords = ['USER_WEATHER','USER_TEMP','USER_RAIN','USER_HIGH_TEMP','USER_LOW_TEMP']
        for kw in keywords:
            if unit.hasIntent(parsed,kw):
                return True


