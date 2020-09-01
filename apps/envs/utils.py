# -*- coding: utf-8 -*-

import re

from .models import Envs


def handle_env(datas):
    datas_list = []
    for item in datas:
        # 将create_time 进行格式化
        # '2019-06-24T09:51:16.038026+08:00' 转化为 '2019-06-24 09:51:16'
        mtch = re.search(r'(.*)T(.*)\..*?', item['create_time'])
        item['create_time'] = mtch.group(1) + ' ' + mtch.group(2)
        datas_list.append(item)
    return datas_list
