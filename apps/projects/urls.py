# -*- coding: utf-8 -*-

from django.urls import path, include
from rest_framework import routers

from projects.views import ProjectsViewSet

'''1. 创建DefaultRouter路由对象'''
router = routers.DefaultRouter()
'''
2. 注册路由
# 第一个参数prefix为路由前缀, 一般添加为应用名即可
# 第二个参数viewset为视图集, 不要加as_view()
'''
router.register(prefix=r'projects', viewset=ProjectsViewSet)

'''
子应用路由表
①每一个子应用(模块)都会维护一个子路由(当前子应用的路由信息表)
②跟主路由表的匹配规则一样，都是从上往下进行匹配
③能匹配上，则执行path第二个参数指定的视图函数，匹配不上，则抛出404异常
'''
# urlpatterns = [
#     path('', index),
#     path('index/', index),
#     如果为类视图, path第二个参数为类视图名.as_view()
#     path('', views.IndexView.as_view()),
#     path('<int:pk>/', views.IndexView.as_view())
#     int为路径参数类型转化器
#     :左边为转换器, 右边为参数别名
#     path('projects/', views.ProjectsList.as_view()),
#     path('projects/<int:pk>/', views.ProjectsDetail.as_view()),
#     path('projects/', views.ProjectsViewSet.as_view({
#         'get': 'list',
#         'post': 'create',
#     }), name='proejcts-list'),
#     path('projects/<int:pk>/', views.ProjectsViewSet.as_view({
#         'get': 'retrieve',
#         'put': 'update',
#         'delete': 'destroy'
#     })),
#
#     path('projects/names/', views.ProjectsViewSet.as_view({
#         'get': 'names',
#     }), name='proejcts-names'),
#
#     path('projects/<int:pk>/interfaces/', views.ProjectsViewSet.as_view({
#         'get': 'interfaces',
#     })),
# ]
'''
3.自动生成路由表
自动生成路由方法①, 添加到urlpatterns中
'''
urlpatterns = [path('', include(router.urls)),]
'''
# 自动生成路由方法②
# 将自动生成的路由，添加到urlpatterns中
'''
# urlpatterns += router.urls
