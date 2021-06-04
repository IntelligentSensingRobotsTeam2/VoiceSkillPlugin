# -*- coding: utf-8-*-
# spray disinfectant
import os
from robot import logging
from robot.sdk.AbstractPlugin import AbstractPlugin
from cmdRecv import udp_send
import time

logger = logging.getLogger(__name__)

class Plugin(AbstractPlugin):

    def handle(self, text, parsed):
        action = ['打开','开始','关闭','停止','停下来']
        result = -1
        timePass = time.time() - self.con.adminState
        adminValid = (timePass) < 20

        print('adminValid:',adminValid)
        for itr,ac in enumerate(action):
            if ac in text:
                result = itr
                break
        if not adminValid:
            self.say(u'抱歉，当前没有管理员权限', cache=True)
            print('time pass:',timePass)
            return 

        if result == -1:
            self.say(u'抱歉，我没有获取到执行动作', cache=True)
        else:
            words = '准备'+action[result] + '消毒工作'
            self.say(words, cache=True)
            if result <= 2:
                udp_send.send_data('spray:True')
            else:
                udp_send.send_data('spray:False')

    def isValid(self, text, parsed):
        # print('parsed:',parsed)
        return any(word in text for word in [u"消毒", u"喷洒",u'停下来'])
