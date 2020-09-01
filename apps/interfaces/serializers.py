from rest_framework import serializers

from .models import Interfaces
from projects.models import Projects
from utils import validates


class InterfacesSerializer(serializers.ModelSerializer):
    """
    接口序列化器
    """
    project = serializers.StringRelatedField(help_text='项目名称')
    # 如果使用了PrimaryKeyRelatedField会自动将前端传入的projectId转化为Projects模型类对象
    project_id = serializers.PrimaryKeyRelatedField(queryset=Projects.objects.all(), help_text='项目ID')

    class Meta:
        model = Interfaces
        fields = ('id', 'name', 'tester', 'project', 'project_id', 'desc', 'create_time')
        # exclude = ('update_time', 'is_delete')

        extra_kwargs = {
            'create_time': {
                'read_only': True
            }
        }

    def create(self, validated_data):
        project = validated_data.pop('project_id')
        validated_data['project'] = project
        interface = Interfaces.objects.create(**validated_data)
        return interface

    def update(self, instance, validated_data):
        if 'project_id' in validated_data:
            project = validated_data.pop('project_id')
            validated_data['project'] = project

        return super().update(instance, validated_data)


class InterfaceRunSerializer(serializers.ModelSerializer):
    """
    通过接口来运行测试用例序列化器
    """
    env_id = serializers.IntegerField(write_only=True,
                                      help_text='环境变量ID',
                                      validators=[validates.whether_existed_env_id])

    class Meta:
        model = Interfaces
        fields = ('id', 'env_id')
