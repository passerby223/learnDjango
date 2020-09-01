# -*- coding: utf-8 -*-

from rest_framework import serializers

from .models import Envs


class EnvsSerializer(serializers.ModelSerializer):
    """
    环境变量序列化器
    """

    class Meta:
        model = Envs
        fields = ('id', 'name', 'base_url', 'desc', 'create_time')
        extra_kwargs = {
            'create_time': {
                'read_only': True
            }
        }


class EnvNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Envs
        fields = ('id', 'name')
