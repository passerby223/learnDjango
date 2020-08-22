# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2019/6/27 9:33 
  @Auth : 可优
  @File : utils.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
-------------------------------------------------
"""
import re

from interfaces.models import Interfaces
from testsuits.models import Testsuits
from testcases.models import Testcases


def modify_output(datas):
    datas_list = []
    for item in datas:
        # 将create_time 进行格式化
        # '2019-06-24T09:51:16.038026+08:00' 转化为 '2019-06-24 09:51:16'
        mtch1 = re.search(r'(.*)T(.*)\..*?', item['create_time'])
        item['create_time'] = mtch1.group(1) + ' ' + mtch1.group(2)

        # update_time 进行格式化
        mtch2 = re.search(r'(.*)T(.*)\..*?', item['update_time'])
        item['update_time'] = mtch2.group(1) + ' ' + mtch2.group(2)

        datas_list.append(item)
    return datas_list


# def get_interfaces_by_ids(ids_list):
#     """
#     通过接口id值组成的列表, 获取所有接口信息
#     :param ids_list: 列表, 例如: [1, 2, 3]
#     :return: 嵌套字典的列表
#     """
#     one_list = []
#     for key in ids_list:
#         try:
#             interface_obj = Interfaces.objects.get(id=key)
#         except Exception as e:
#             continue
#         one_list.append({
#             'id': interface_obj.id,
#             'name': interface_obj.name
#         })
#
#     return one_list


def get_testcases_by_interface_ids(ids_list):
    """
    通过接口id获取用例
    :param ids_list:
    :return:
    """
    one_list = []
    for interface_id in ids_list:
        testcases_qs = Testcases.objects.values_list('id', flat=True).\
            filter(interface_id=interface_id, is_delete=False)
        one_list.extend(list(testcases_qs))
    return one_list
