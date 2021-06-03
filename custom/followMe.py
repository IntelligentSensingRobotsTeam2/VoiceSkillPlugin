# -*- coding: utf-8-*-
# spray disinfectant
import os
from robot.sdk import unit
from robot import logging
from robot.sdk.AbstractPlugin import AbstractPlugin

logger = logging.getLogger(__name__)

class Plugin(AbstractPlugin):

    def handle(self, text, parsed):
        def onAsk(input,place_name):
            if input is None:
                self.say(u'已取消')
                return

            if any(word in input for word in [u"是的", u"对的"]):
                self.say('跟我走，我带你去{}'.format(place_name))
                return
            elif any(word in input for word in [u"不是", u"错"]):
                self.say('抱歉，请重新讲一遍吧')
                return
            else :
                print('input:',input)
                self.say('抱歉，我没听清')
                return
        slots = unit.getSlots(parsed, 'WHERETOGO')  # 取出所有词槽
        # 遍历词槽，找出 user_place 对应的值
        for slot in slots:
            if slot['name'] == 'user_place':
                self.say('请问您是要去{}吗'.format(slot['normalized_word']),
                 cache=True, onCompleted=lambda: onAsk(self.activeListen(),slot['normalized_word']))
                # self.say('去{}请跟我走！'.format(slot['normalized_word']))
                return
        # 如果没命中词槽
        self.say("请问是去哪里", cache=True, onCompleted=lambda: onAsk(self.activeListen(),slot['normalized_word']))

    def isValid(self, text, parsed):
        # print('parsed:',parsed)
        return unit.hasIntent(parsed, 'WHERETOGO')
        # return any(word in text for word in [u"怎么走", u"怎么去",u'在哪里',u'我想去',u'在哪儿'])
