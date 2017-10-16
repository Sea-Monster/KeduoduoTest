# -*- coding: utf-8 -*-
import json
from .settings import *
import logging

logging.basicConfig(level=logging.INFO)


def debug(msg, *args, **kwargs):
    return logging.debug(msg, *args, **kwargs)


def error(msg, *args, **kwargs):
    return logging.error(msg, *args, **kwargs)


def warning(msg, *args, **kwargs):
    return logging.warning(msg, *args, **kwargs)


def info(msg, *args, **kwargs):
    return logging.info(msg, *args, **kwargs)


def convert_to_json(obj):
    s = str(obj)
    json_str = json.dumps(s, ensure_ascii=False, indent='\t')
    # print(json_obj)
    # print(type(json_obj))
    return json_str


def export_dict_to_json(dict_obj, filename, filepath=LOGS_PATH):
    with open(filepath + filename, mode='w') as sess:
        # sess.write(s)
        json.dump(dict_obj, sess, ensure_ascii=False, indent='\t')


def export_logs(obj, filename, filepath=LOGS_PATH):
    if isinstance(obj, str):
        s = obj
    else:
        s = convert_to_json(obj)
    with open(filepath + filename, mode='w') as sess:
        # sess.write(s)
        json.dump(obj._asdict(), sess, ensure_ascii=False, indent='\t')


if __name__ == '__main__':
    pass
