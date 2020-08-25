from rest_framework import serializers

from .models import Projects
from debugtalks.models import DebugTalks
from interfaces.models import Interfaces
from utils import validates


class ProjectModelSerializer(serializers.ModelSerializer):

    class Meta:
        # 1. 指定参考哪个模型类来创建模型类序列化器
        model = Projects
        '''
        2. 指定为模型类的哪些字段(__all__指定模型类中的所有字段)，来生成序列化器;默认DRF会自动创建模型类的ID字段的read_only=True属性
        ①如果需要模型类的所有字段来生成模型类序列化器，则指定fields='__all__'，此时fields的值只能是`字符串`类型
        ②如果需要模型类的部分字段来生成模型类序列化器，则指定fields=(字段1, 字段2, ...)，此时fields的值只能是`元组`类型
        ③如果需要`除了模型类的部分字段外的其它字段`来生成模型类序列化器，则指定exclude=(字段1, 字段2, ...)，此时exclude的值只能是`元组`类型
        ④如果需要模型类的部分字段设置`read_only=True`属性，则指定read_only_fields=(字段1, 字段2, ...)，此时read_only_fields的值只能是`元组`类型
        '''
        exclude = ('update_time', 'is_delete')
        '''
        3. 使用extra_kwargs为字段添加其他属性:例如`write_only`属性需要通过这种方式来添加
           read_only=True指定该字段只能进行序列化输出,不进行反序列化输入
           write_only=True指定该字段只能进行反序列化输入,不进行序列化输出
           如果不指定read_only=True的字段，默认既可以进行序列化输出，又可以进行反序列化输入
        '''
        extra_kwargs = {
            'create_time': {
                'read_only': True
            }
        }

    def create(self, validated_data):
        project_obj = super().create(validated_data)
        DebugTalks.objects.create(project=project_obj)

        return project_obj


class ProjectNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ('id', 'name')


class InterfaceNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interfaces
        fields = ('id', 'name', 'tester')


class InterfacesByProjectIdSerializer(serializers.ModelSerializer):
    interfaces = InterfaceNameSerializer(read_only=True, many=True)

    class Meta:
        model = Projects
        fields = ('id', 'interfaces')


class ProjectsRunSerializer(serializers.ModelSerializer):
    """
    通过项目运行测试用例序列化器
    """
    env_id = serializers.IntegerField(write_only=True,
                                      help_text='环境变量ID',
                                      validators=[validates.whether_existed_env_id])

    class Meta:
        model = Projects
        fields = ('id', 'env_id')
