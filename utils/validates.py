# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2019/6/29 17:35 
  @Auth : 可优
  @File : validates.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
-------------------------------------------------
"""
from rest_framework import serializers

from projects.models import Projects
from interfaces.models import Interfaces
from envs.models import Envs


def whether_existed_project_id(value):
    """
    检查项目id是否存在
    :param value:
    :return:
    """
    if not isinstance(value, int):
        raise serializers.ValidationError('所选项目有误!')
    elif not Projects.objects.filter(is_delete=False, id=value).exists():
            raise serializers.ValidationError('所选项目不存在!')


def whether_existed_interface_id(value):
    """
    检查项目id是否存在
    :param value:
    :return:
    """
    if not isinstance(value, int):
        raise serializers.ValidationError('所选接口有误!')
    elif not Interfaces.objects.filter(is_delete=False, id=value).exists():
            raise serializers.ValidationError('所选接口不存在!')


def whether_existed_env_id(value):
    """
    检查环境配置id是否存在
    :param value:
    :return:
    """
    if value != 0:
        if not Envs.objects.filter(is_delete=False, id=value).exists():
                raise serializers.ValidationError('所选环境配置不存在!')
