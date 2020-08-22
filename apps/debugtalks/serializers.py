# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2019/6/28 17:48 
  @Auth : 可优
  @File : serializers.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
-------------------------------------------------
"""
from rest_framework import serializers

from .models import DebugTalks


class DebugTalksSerializer(serializers.ModelSerializer):
    """
    DebugTalks序列化器
    """
    project = serializers.StringRelatedField(help_text='项目名称')

    class Meta:
        model = DebugTalks
        exclude = ('is_delete', 'create_time', 'update_time')
        read_only_fields = ('name', 'project')

        extra_kwargs = {
            'debugtalk': {
                'write_only': True
            }
        }
