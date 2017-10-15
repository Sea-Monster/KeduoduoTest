# -*- coding: utf-8 -*-
import configparser

cf = configparser.ConfigParser()
cf.read('/Users/SeaMonster/PycharmProjects/KeduoduoTest/settings.conf')
IMAGE_PATH = '/Users/SeaMonster/PycharmProjects/KeduoduoTest/images/'
IMAGE_SUBFIX_DEFAULT = '.png'
LOGS_PATH = '/Users/SeaMonster/PycharmProjects/KeduoduoTest/logs/'
USER_NAME = cf.get('AUTH','user_name')
PASSWORD = cf.get('AUTH','password')
