import os
from datetime import datetime

from django.conf import settings
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework import status

from . import serializers
from .models import Projects
from .utils import get_count_by_project
from interfaces.models import Interfaces
from testcases.models import Testcases
from envs.models import Envs
from utils import common


class ProjectsViewSet(ModelViewSet):
    """
    list:
    返回项目(多个)列表数据(包含项目下的聚合数据：接口数,用例数,套件数,配置数)

    create:
    创建项目

    retrieve:
    返回项目(单个)详情数据

    update:
    更新(全部)项目

    partial_update:
    更新(部分)项目

    destroy:
    删除单个项目

    names:
    返回所有项目的ID和名称

    interfaces:
    返回某个项目的所有接口信息(ID和名称)
    """
    '''
    上边的多行注释中的`字段`对应每个`action`，`字段对应的值`为`接口文档页面`中展示的`接口描述信息`
    如果继承APIView或GenericAPIView的话。下边的方法必须定义为get、post、put、delete等请求方法，这些请求方法全放到一个类中会有冲突。
    所以需要使用viewsets.ViewSet来定义action动作
    ViewSet不支持get、post、put、delete请求方法，只支持action动作
    但是ViewSet中未提供get_object(), get_serializer()等方法(因为ViewSet类不会继承GenericAPIView类)，所以需要继承GenericViewSet类
    ModelViewSet又继承了GenericViewSet类。
    ModelViewSet类默认提供了`create()`, `retrieve()`, `update()`, `partial_update()`, `destroy()`和`list()`这些actions
    '''
    '''
    1.指定查询集，queryset用于指定需要使用的查询集
    获取到未被软删除的数据的查询集
    '''
    queryset = Projects.objects.filter(is_delete=False)
    '''2.指定序列化器，serializer_class指定需要使用到的序列化器类'''
    serializer_class = serializers.ProjectModelSerializer
    '''3.指定projects视图的权限类，需要被授权才能访问'''
    permission_classes = (permissions.IsAuthenticated, )
    '''4.指定需要排序的字段,排序功能必须配合过滤引擎才可以正常使用'''
    ordering_fields = ('id', 'name')
    '''5.在视图类中指定过滤引擎,也可以在setting.py文件中全局指定过滤引擎，如果全局指定了过滤引擎，这里就不需要再次指定了。'''
    # filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    # filterset_fields = ['name', 'leader', 'tester']

    def perform_destroy(self, instance):
        instance.is_delete = True
        instance.save()   # 逻辑删除

    '''
    1.可以使用action装饰器来声明自定义action动作，默认情况下，实例方法名就是action动作名
    2.methods参数用于指定该action支持的请求方法，默认是get方法
    3.detail参数用于指定该action要处理的是是否是详情资源对象(ps:url是否需要传递pk值,是的话传True，不是的话传False)
    '''
    @action(methods=['get'], detail=False)
    def names(self, request, *args, **kwargs):
        # 1.使用get_queryset()获取查询集的所有数据;get_queryset()方法获取到的是重写后的`queryset`类属性
        queryset = self.get_queryset()
        '''
        2.获取序列化器类并传入查询集实例(因为返回的查询集是多条数据，需要设置many=True)
        这里get_serializer()方法获取到的是重写后的`serializer_class`类属性
        '''
        serializer = self.get_serializer(instance=queryset, many=True)
        '''
        3.将序列化器生成的序列化数据返回给前端
        '''
        return Response(serializer.data)

    @action(methods=['get'], detail=True)
    def interfaces(self, request, pk=None):
        # 获取单个project下的所有interfaces列表数据
        # 这里为什么要使用project_id?
        # 因为project_id是interfaces表的外键字段，关联着projects表的id字段
        interface_objs = Interfaces.objects.filter(project_id=pk, is_delete=False)
        '''
        此处不能使用self.get_serializer(),如果使用它获取到的是ProjectModelSerializer序列化器,而不是InterfacesByProjectIdSerializer序列化器
        但是我们只需要返回project下所有interfaces接口的ID和name即可,不需要全部返回。所以使用下边的方法返回数据。
        '''
        # serializer = serializers.InterfacesByProjectIdSerializer(instance=self.get_object())
        # return Response(serializer.data)
        one_list = []
        for obj in interface_objs:
            one_list.append({
                'id': obj.id,
                'name': obj.name
            })
        return Response(data=one_list)

    def list(self, request, *args, **kwargs):
        # queryset = self.filter_queryset(self.get_queryset())
        #
        # page = self.paginate_queryset(queryset)
        # if page is not None:
        #     serializer = self.get_serializer(page, many=True)
        #     datas = serializer.data
        #     datas = get_count_by_project(datas)
        #     return self.get_paginated_response(datas)
        #
        # serializer = self.get_serializer(queryset, many=True)
        # datas = serializer.data
        # datas = get_count_by_project(datas)
        # return Response(datas)
        response = super().list(request, *args, **kwargs)
        response.data['results'] = get_count_by_project(response.data['results'])
        return response

    # def get_serializer_class(self):
    #     if self.action == 'names':
    #         return serializers.ProjectNameSerializer
    #     else:
    #         return self.serializer_class

    @action(methods=['post'], detail=True)
    def run(self, request, pk=None):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        datas = serializer.validated_data
        env_id = datas.get('env_id')  # 获取环境变量env_id

        # 创建测试用例所在目录名
        testcase_dir_path = os.path.join(settings.SUITES_DIR,
                                         datetime.strftime(datetime.now(), "%Y%m%d%H%M%S%f"))
        if not os.path.exists(testcase_dir_path):
            os.mkdir(testcase_dir_path)

        env = Envs.objects.filter(id=env_id, is_delete=False).first()
        interface_objs = Interfaces.objects.filter(is_delete=False, project=instance)

        if not interface_objs.exists():  # 如果此项目下没有接口, 则无法运行
            data_dict = {
                "detail": "此项目下无接口, 无法运行!"
            }
            return Response(data_dict, status=status.HTTP_400_BAD_REQUEST)

        for inter_obj in interface_objs:
            testcase_objs = Testcases.objects.filter(is_delete=False, interface=inter_obj)

            for one_obj in testcase_objs:
                common.generate_testcase_files(one_obj, env, testcase_dir_path)

        # 运行用例
        return common.run_testcase(instance, testcase_dir_path)

    def get_serializer_class(self):
        """
        不同的action选择不同的序列化器
        :return:
        """
        if self.action == 'names':
            return serializers.ProjectNameSerializer
        elif self.action == 'run':
            return serializers.ProjectsRunSerializer
        else:
            return self.serializer_class
