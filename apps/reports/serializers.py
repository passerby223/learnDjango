# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2019/11/8 21:30 
  @Auth : 可优
  @File : serializers.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: keyou100@qq.com
  @Company: 湖南省零檬信息技术有限公司
  @Copyright: 柠檬班
-------------------------------------------------
"""
from datetime import datetime
from rest_framework import serializers

from .models import Reports


class ReportsSerializer(serializers.ModelSerializer):
    """
    报告序列化器
    """

    class Meta:
        model = Reports
        exclude = ('update_time', 'is_delete')

        extra_kwargs = {
            'html': {
                'write_only': True
            },
            'create_time': {
                'read_only': True
            }
        }

    # def create(self, validated_data):
    #     report_name = validated_data['name']
    #     validated_data['name'] = report_name + '_' + datetime.strftime(datetime.now(), '%Y%m%d%H%M%S')
    #     report = Reports.objects.create(**validated_data)
    #     return report
