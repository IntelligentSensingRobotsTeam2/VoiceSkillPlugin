# -*- coding: utf-8-*-
# turn on / off robot admin mode.
import os,time
from robot.sdk import unit
from robot import logging
from robot.sdk.AbstractPlugin import AbstractPlugin

logger = logging.getLogger(__name__)

class Plugin(AbstractPlugin):

    def handle(self, text, parsed):
        if input is None:
            self.say(u'抱歉，我没有获取到执行动作.')
            return
        adminValid = self.con.adminSwitch

        print('adminValid:',adminValid)
        if adminValid:
            if any(word in text for word in [u"开启", u"打开"]):
                self.con.autoRotate = True
                self.say('自动旋转已开启')
                return
            elif any(word in text for word in [u"关闭", u"取消"]):
                self.con.autoRotate = False
                self.say('自动旋转已关闭')
                return
        else:
            self.say('抱歉，当前没有管理员权限')
        
    def isValid(self, text, parsed):
        # print('parsed:',parsed)
        # return unit.hasIntent(parsed, 'WHERETOGO')
        # print('text:',text)
        return any(word in text for word in [u"自动旋转", u"自动转向"])
