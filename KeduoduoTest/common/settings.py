# -*- coding: utf-8 -*-
import configparser
import os

__all__= ['IMAGE_PATH','IMAGE_SUBFIX_DEFAULT','LOGS_PATH','USER_NAME','PASSWORD','BASE_URL','BASE_LOGIN_URL','NO_PIC']

_cf = configparser.ConfigParser()
_cf.read(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + '/settings.conf')
IMAGE_PATH = _cf.get('OUTPUT', 'image_path')
IMAGE_SUBFIX_DEFAULT = _cf.get('OUTPUT', 'image_default_subfix')
LOGS_PATH = _cf.get('OUTPUT', 'logs_path')
USER_NAME = _cf.get('AUTH', 'user_name')
PASSWORD = _cf.get('AUTH', 'password')
BASE_URL = _cf.get('URL', 'base_url')
BASE_LOGIN_URL = _cf.get('URL', 'base_login_url')
NO_PIC = False if _cf.get('WEB_SETTING', 'no_pic') == '0' else True
