# -*- coding: utf-8-*-
# spray disinfectant
import os
from robot import logging
from robot.sdk.AbstractPlugin import AbstractPlugin

logger = logging.getLogger(__name__)

class Plugin(AbstractPlugin):

    def handle(self, text, parsed):
        action = ['打开','开始','关闭','停止','停下来']
        result = -1

        for itr,ac in enumerate(action):
            if ac in text:
                result = itr
                break

        if result == -1:
            self.say(u'抱歉，我没有获取到执行动作', cache=True)
        else:
            words = '准备'+action[result] + '消毒工作'
            self.say(words, cache=True)

    def isValid(self, text, parsed):
        # print('parsed:',parsed)
        return any(word in text for word in [u"消毒", u"喷洒",u'停下来'])
