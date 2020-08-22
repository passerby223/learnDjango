import re

from django.db.models import Count

from interfaces.models import Interfaces


def get_count_by_interface(datas):
    datas_list = []
    for item in datas:
        # 将create_time 进行格式化
        # '2019-06-24T09:51:16.038026+08:00' 转化为 '2019-06-24 09:51:16'
        mtch = re.search(r'(.*)T(.*)\..*?', item['create_time'])
        item['create_time'] = mtch.group(1) + ' ' + mtch.group(2)

        interface_id = item['id']
        # 计算用例数
        interfaces_testcases_objs = Interfaces.objects.values('id').annotate(testcases=Count('testcases')). \
            filter(id=interface_id, is_delete=False)
        testcases_count = 0
        for one_dict in interfaces_testcases_objs:
            testcases_count += one_dict['testcases']

        # 计算配置数
        interfaces_configures_objs = Interfaces.objects.values('id').annotate(configures=Count('configures')). \
            filter(id=interface_id, is_delete=False)
        config_count = 0
        for i in interfaces_configures_objs:
            config_count += i['configures']

        # 计算套件数
        item['testcases'] = testcases_count
        item['configures'] = config_count
        datas_list.append(item)
    return datas_list
