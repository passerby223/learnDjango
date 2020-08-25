# -*- coding: utf-8 -*-

import re

from django.db.models import Count

from interfaces.models import Interfaces
from testsuits.models import Testsuits


def get_count_by_project(datas):
    datas_list = []
    for item in datas:
        # 格式化时间戳
        mtch = re.search(r'(.*)T(.*)\..*?', item['create_time'])
        # 对正则提取出来的字符串进行拼接重新赋值给item['create_time']
        item['create_time'] = mtch.group(1) + ' ' + mtch.group(2)
        # 取出每一个projectId
        project_id = item['id']
        # Interfaces.objects.filter(project_id=project_id, is_delete=False)
        '''
        ①通过`values('id')`方法以`tb_interfaces`表中的`id`字段进行分组；
        ②通过`annotate(testcases=Count('testcases')`来对`tb_interfaces`表中的每个接口下的用例进行聚合操作
        PS：
        `testcases`为聚合操作生成的数据集的别名;
        `Count('testcases')`中的testcases为`tb_interfaces`表的外键表`tb_testcases`表对应的模型类名小写`testcases`
        ③通过filter()方法对聚合后的数据进行过滤。过滤后的数据需要满足is_delete=False，即未被软删除
        '''
        interfaces_testcases_objs = Interfaces.objects.values('id').annotate(testcases=Count('testcases')).\
            filter(project_id=project_id, is_delete=False)
        '''interfaces_count：当前project下的interfaces数量'''
        interfaces_count = interfaces_testcases_objs.count()
        testcases_count = 0
        for one_dict in interfaces_testcases_objs:
            # 通过遍历查询集中的数据，取出每个interface下的testcase数量进行累加，即project下的总testcase数量
            testcases_count += one_dict['testcases']

        '''求project下的configs配置的数量，计算逻辑与`计算project下的总testcase数量`逻辑一致'''
        interfaces_configures_objs = Interfaces.objects.values('id').annotate(configures=Count('configures')). \
            filter(project_id=project_id, is_delete=False)
        configures_count = 0
        for one_dict in interfaces_configures_objs:
            configures_count += one_dict['configures']
        '''获取当前project下的testsuites的总数量'''
        testsuits_count = Testsuits.objects.filter(project_id=project_id, is_delete=False).count()

        item['interfaces'] = interfaces_count
        item['testsuits'] = testsuits_count
        item['testcases'] = testcases_count
        item['configures'] = configures_count

        datas_list.append(item)
    # 将聚合统计后的数据返回
    return datas_list

