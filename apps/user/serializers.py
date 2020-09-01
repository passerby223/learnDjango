# -*- coding: utf-8 -*-

from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User


class RegisterSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(label='确认密码', help_text='确认密码',
                                             min_length=6, max_length=20,
                                             write_only=True,
                                             error_messages={
                                                 'min_length': '仅允许6~20个字符的确认密码',
                                                 'max_length': '仅允许6~20个字符的确认密码', })
    token = serializers.CharField(label='生成token', read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'password_confirm', 'token')
        extra_kwargs = {
            'username': {
                'label': '用户名',
                'help_text': '用户名',
                'min_length': 6,
                'max_length': 20,
                'error_messages': {
                    'min_length': '仅允许6-20个字符的用户名',
                    'max_length': '仅允许6-20个字符的用户名',
                }
            },
            'email': {
                'label': '邮箱',
                'help_text': '邮箱',
                'write_only': True,
                'required': True,
                # 添加邮箱重复校验
                'validators': [UniqueValidator(queryset=User.objects.all(), message='此邮箱已注册')],
            },
            'password': {
                'label': '密码',
                'help_text': '密码',
                'write_only': True,
                'min_length': 6,
                'max_length': 20,
                'error_messages': {
                    'min_length': '仅允许6-20个字符的密码',
                    'max_length': '仅允许6-20个字符的密码',
                }
            }
        }

    def validate(self, attrs):
        password = attrs.get('password')
        password_confirm = attrs.get('password_confirm')
        if password != password_confirm:
            raise serializers.ValidationError('两次输入密码不正确')
        return attrs

    def create(self, validated_data):
        # 移除数据库模型类中不存在的属性
        validated_data.pop('password_confirm')
        user = User.objects.create_user(**validated_data)
        # user = super(RegisterSerializers, self).create(**validated_data)
        # user.set_password(validated_data['password'])   # 设置密码
        # user.save()

        # 创建手动创建token
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        user.token = token
        return user

# 接口测试
# 有哪些方法?
# 1. 工具, postman
# 2. 使用代码创建接口测试框架
# 用例数据存放咋哪里? excel
# unittest + ddt 数据驱动, 测试数据与测试代码分离
# 日志器
# 配置文件
# pymysql
# requests
# 参数化, 正则匹配
# 接口依赖, 动态创建类属性的方式来处理
# 生成报告
# Jenkins实现持续集成

# HttpRunner, 将上述所有优秀的框架进行了完美地封装, 几乎可以零代码, 高效率进行接口测试
# json或者yaml格式的形式来表现
