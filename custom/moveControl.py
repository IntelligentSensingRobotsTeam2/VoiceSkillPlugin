# -*- coding: utf-8-*-
# control robot movement.

import os
from robot.sdk import unit
from robot import logging
from robot.sdk.AbstractPlugin import AbstractPlugin
from cmdRecv import udp_send
import time
import re

logger = logging.getLogger(__name__)

class Plugin(AbstractPlugin):
    # self.
    def handle(self, text, parsed):
        adminValid = self.con.adminSwitch 

        print('adminValid:',adminValid)
        if not adminValid:
            self.say(u'抱歉，当前没有管理员权限', cache=True)
            return

        direction = ''
        value = 0
        action = ''
        inverse = False

        if unit.hasIntent(parsed,'ROBOT_WALK'):    
            slots = unit.getSlots(parsed, 'ROBOT_WALK')  # 取出所有词槽
            # 遍历词槽，找出 user_person 对应的值
            for slot in slots:
                if slot['name'] == 'user_direction':
                    direction = slot['normalized_word']
                    if direction == 'forward':
                        action = '向前走'
                    elif direction == 'backward':
                        action = '向后走'
                        direction = 'forward'
                        inverse = True
                if slot['name'] == 'user_generic_unit':
                    value = int(float(slot['normalized_word'].split('|')[0]))

            
            if value <-6 or value > 6:
                self.say('超出可行移动范围')
                return 

            self.say('我将要{}{}米'.format(action,value))
        

        elif unit.hasIntent(parsed,'ROBOT_TURN'): 

            slots = unit.getSlots(parsed, 'ROBOT_TURN')  # 取出所有词槽
            for slot in slots:
                if slot['name'] == 'user_direction':
                    direction = slot['normalized_word']
                    if direction == 'left':
                        action = '逆时针转'
                        direction = 'rotate'
                        inverse = True

                    elif direction == 'right':
                        action = '顺时针转'
                        direction = 'rotate'

                if slot['name'] == 'user_generic_unit':
                    value = int(float(slot['normalized_word'].split('|')[0]))

            if value <-180 or value > 180:
                self.say('超出可行移动范围')
                return
            
            self.say('我将要{}{}度'.format(action,value))
            
        if inverse:
            value = -value

        udp_send.send_data('{}:{}'.format(direction,value))
            # for slot in slots:
            #     if slot['name'] == 'user_direction':
            #         print('')

            # if result <= 2:
            #     udp_send.send_data('spray:1')
            # else:
            #     udp_send.send_data('spray:0')

    def isValid(self, text, parsed):
        keywords = ['ROBOT_WALK','ROBOT_TURN']
        for kw in keywords:
            if unit.hasIntent(parsed,kw):
                return True
