# -*- coding: utf-8 -*-
import os


def check_directory_exist(path):
    return os.path.exists(path)


def make_directory(path):
    """

    :type path: str
    """
    # path_lst = path.split('/')
    # path_full = ''
    # for s in path_lst:
    #     if s is None or s == '':
    #         continue
    #     else:
    #         path_full = path_full + '/' + s
    #         print('FULL PATH: ' + path_full)
    #         if not os.path.exists(path_full):
    #             os.mkdir()
    #
    #

    os.makedirs(path, exist_ok=True)
