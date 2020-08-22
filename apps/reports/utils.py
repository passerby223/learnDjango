# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2019/11/8 21:39 
  @Auth : 可优
  @File : utils.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: keyou100@qq.com
  @Company: 湖南省零檬信息技术有限公司
  @Copyright: 柠檬班
-------------------------------------------------
"""
from datetime import datetime
import re

from django.db.models import Count


def format_output(datas):
    datas_list = []
    for item in datas:
        result = 'Pass' if item['result'] else 'Fail'

        mtch = re.search(r'(.*)T(.*)\..*?', item['create_time'])
        item['create_time'] = mtch.group(1) + ' ' + mtch.group(2)

        item['result'] = result
        datas_list.append(item)
    return datas_list


def get_file_contents(filename, chunk_size=512):
    with open(filename, encoding='utf-8') as f:
        while True:
            c = f.read(chunk_size)
            if c:
                yield c
            else:
                break
