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
        timePass = time.time() - self.con.adminState
        adminValid = (timePass) < 20

        print('adminValid:',adminValid)
        if adminValid:
            if any(word in text for word in [u"开启", u"打开"]):
                self.con.adminSwitch = True
                self.say('管理员权限已开启')
                return
            elif any(word in text for word in [u"关闭", u"取消"]):
                self.con.adminSwitch = False
                self.say('管理员权限已关闭')
                return
        else:
            self.say('请先在相机前认证管理员')
        
    def isValid(self, text, parsed):
        # print('parsed:',parsed)
        # return unit.hasIntent(parsed, 'WHERETOGO')
        # print('text:',text)
        return any(word in text for word in [u"管理员", u"权限",u'模式'])
